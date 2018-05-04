import subprocess
import time
import unittest
import platform
from functools import partial
from multiprocessing import Pool

from libs.case_builder import TestInterfaceCase
from libs.console import console_out
from libs.create_directory import create_server_log_dir, create_appium_log_dir, create_node_json_dir, create_temp_dir
from libs.get_device_info import devices_list
from libs.node_json_creator import node_json_create
from testcases.test import CalculatorTest


def kill_process(process_name):
    system = platform.system()
    if system == 'Darwin' or system == 'Linux':
        subprocess.Popen('killall %s' % process_name, shell=True)
    elif system == 'Windows':
        subprocess.Popen('taskkill /F /IM %s.exe /T' % process_name, shell=True)


def kill_jar(jar_name):
    jar_running = subprocess.Popen("jps -mlv | grep " + jar_name, stdout=subprocess.PIPE, shell=True).stdout.read()
    try:
        jar_pid = (jar_running.split()[0]).decode()
        subprocess.Popen("kill " + jar_pid, shell=True)
    except IndexError:
        console_out(jar_name + " is not running.")


def init_selenium_server(start_time):
    save_log = create_server_log_dir(start_time) + "selenium_server_" + \
               time.strftime('%Y.%m.%d_%H-%M-%S', time.localtime()) + ".log"
    with open(create_temp_dir(create_time) + "selenium_running_output.log", "w") as file:
        subprocess.Popen("java -jar ./libs/selenium-server-standalone-3.10.0.jar -port 4444 -role hub -log " + save_log,
                         stdout=file, stderr=None, shell=True)
    console_out("Selenium server started, log saved in %s" % save_log)


def start_appium_server(device_id, i, start_time):
    port = 4500 + i * 10
    bootstrap_port = port + 1
    node_json_create(start_time, device_id, "127.0.0.1", str(port))
    save_node_json = create_node_json_dir(start_time) + device_id + '.json'
    save_log = \
        create_appium_log_dir(start_time) + "appium_server_" + device_id + "_" + \
        time.strftime('%Y.%m.%d_%H-%M-%S', time.localtime()) + ".log"
    with open(create_temp_dir(create_time) + "appium_server_" + device_id + "_output.log", "w") as file:
        subprocess.Popen("appium --nodeconfig " + save_node_json + " -p " + str(port) + " -bp " + str(bootstrap_port) +
                         " -g " + save_log, stdout=file, stderr=None, shell=True)
    console_out("%s's appium server started, log saved in %s." % (device_id, save_log))


def init_appium_server(start_time, dut_list):
    pool = Pool(len(dut_list))
    for i in range(len(dut_list)):
        pool.apply_async(start_appium_server, (dut_list[i], i, start_time,))
    pool.close()
    pool.join()


def shutdown_servers():
    kill_jar('selenium')
    kill_process('node')
    console_out('Servers shutdown.')


def run_case(start_time, device_id):
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(
        testcase_class=CalculatorTest,
        create_time=start_time,
        device_id=device_id))
    unittest.TextTestRunner(verbosity=2).run(suite)


def runner_pool(start_time, duts_list):
    partial_run_case = partial(run_case, start_time)
    devices_pool = []
    for i in range(0, len(duts_list)):
        devices_pool.append(duts_list[i])
    pool = Pool(len(duts_list))
    pool.map(partial_run_case, devices_pool)
    pool.close()
    pool.join()


if __name__ == '__main__':
    create_time = time.strftime('%Y.%m.%d_%H-%M-%S', time.localtime())
    DUT_list = devices_list()
    is_ready = False
    while not is_ready:
        start_hint = "\nPlease check all the connections, press Y on the keyboard to start test, " \
                     "press R to restart connection check, press N to exit this test"
        start_input = input(start_hint).strip()
        if start_input.lower() == "y":
            is_ready = True
            kill_jar("selenium")
            kill_process('node')
            init_selenium_server(create_time)
            init_appium_server(create_time, DUT_list)
            console_out("All appium server started, please wait 10s for test started.")
            time.sleep(10)
            console_out('Test started')
            runner_pool(create_time, DUT_list)
            shutdown_servers()
        elif start_input.lower() == "r":
            DUT_list = devices_list()
        elif start_input.lower() == "n":
            break
        else:
            print("Input wrong argument.")

    kill_jar('selenium')
    kill_process('node')

import json
import unittest

from appium import webdriver
from libs.create_directory import create_node_json_dir


def appium_driver(create_time, device_id):
    node_json = str(create_node_json_dir(create_time) + device_id + '.json')
    with open(node_json, 'r', encoding='utf-8') as json_file:
        load_json = json.load(json_file)
    load_capabilities = load_json['capabilities'][0]
    desired_caps = {'platformName': load_capabilities['platformName'],
                    'platformVersion': load_capabilities['platformVersion'],
                    'deviceName': load_capabilities['deviceName'],
                    'appPackage': 'com.android.calculator2',
                    'appActivity': '.Calculator',
                    'udid': load_capabilities['udid'],
                    'unicodeKeyboard': 'true',
                    'resetKeyboard': 'true'}
    # remote = load_json['configuration']['url']
    remote = 'http://127.0.0.1:4444/wd/hub'
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class TestInterfaceCase(unittest.TestCase):
    def __init__(self, case_name='test', create_time=None, device_id=None):
        super(TestInterfaceCase, self).__init__(case_name)
        self.device_id = device_id
        self.create_time = create_time

    def setUp(self):
        self.driver = appium_driver(self.create_time, self.device_id)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    @staticmethod
    def parametrize(testcase_class, create_time, device_id=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_class(name, create_time, device_id))
        return suite

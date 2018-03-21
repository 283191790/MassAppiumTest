import json
import time

from .create_directory import create_node_json_dir
from .get_device_info import model, manufacturer, android_version


def node_json_create(start_time, device_id, host, host_port, grid="127.0.0.1", grid_port="4444"):
    browser_name = model(device_id)
    device_name = model(device_id)
    manufacturer_name = manufacturer(device_id)
    version = android_version(device_id)
    udid = device_id

    node_json = json.dumps(
        {
            "capabilities": [
                {
                    "browserName": browser_name,
                    "udid": udid,
                    "manufacturer": manufacturer_name,
                    "deviceName": device_name,
                    "platformName": "Android",
                    "platformVersion": version,
                    "maxInstances": 1
                }
            ],
            "configuration": {
                "cleanUpCycle": 2000,
                "timeout": 60000,
                "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
                "url": 'http://' + host + ':' + host_port + '/wd/hub',
                "host": host,
                "port": host_port,
                "maxSession": 1,
                "register": True,
                "registerCycle": 5000,
                "hubPort": grid_port,
                "hubHost": grid
            }
        }, sort_keys=False, indent=4, separators=(',', ': '))
    save_node_json = create_node_json_dir(start_time) + device_id + '.json'
    with open(save_node_json, 'w') as file:
        file.write(node_json)
    print(time.ctime() + "~~: Device " + device_id + " node config has created, it's saved in " + save_node_json)

import os


def create_result_dir(create_time):
    result_path = os.path.join(".", "results")
    result_path_is_exists = os.path.exists(result_path)
    if not result_path_is_exists:
        os.makedirs(result_path)
    result_folder = result_path + os.path.sep + create_time
    result_folder_is_exists = os.path.exists(result_folder)
    if not result_folder_is_exists:
        os.makedirs(result_folder)
    return result_folder + os.path.sep


def create_server_log_dir(create_time):
    server_log_dir_path = create_result_dir(create_time)
    server_log_dir_path_is_exists = os.path.exists(server_log_dir_path)
    if not server_log_dir_path_is_exists:
        os.makedirs(server_log_dir_path)
    server_log_folder = server_log_dir_path + os.path.sep + "server_log"
    server_log_folder_is_exists = os.path.exists(server_log_folder)
    if not server_log_folder_is_exists:
        os.makedirs(server_log_folder)
    return server_log_folder + os.path.sep


def create_appium_log_dir(create_time):
    appium_log_dir_path = create_result_dir(create_time)
    appium_log_dir_path_is_exists = os.path.exists(appium_log_dir_path)
    if not appium_log_dir_path_is_exists:
        os.makedirs(appium_log_dir_path)
    appium_log_folder = appium_log_dir_path + os.path.sep + "server_log"
    appium_log_folder_is_exists = os.path.exists(appium_log_folder)
    if not appium_log_folder_is_exists:
        os.makedirs(appium_log_folder)
    return appium_log_folder + os.path.sep


def create_node_json_dir(create_time):
    node_json_dir_path = create_result_dir(create_time)
    node_json_dir_path_is_exists = os.path.exists(node_json_dir_path)
    if not node_json_dir_path_is_exists:
        os.makedirs(node_json_dir_path)
    node_json_folder = node_json_dir_path + os.path.sep + "node_json"
    node_json_folder_is_exists = os.path.exists(node_json_folder)
    if not node_json_folder_is_exists:
        os.makedirs(node_json_folder)
    return node_json_folder + os.path.sep


def create_temp_dir(create_time):
    create_temp_dir_path = create_result_dir(create_time)
    create_temp_dir_path_is_exists = os.path.exists(create_temp_dir_path)
    if not create_temp_dir_path_is_exists:
        os.makedirs(create_temp_dir_path)
    create_temp_folder = create_temp_dir_path + os.path.sep + "temp"
    create_temp_folder_is_exists = os.path.exists(create_temp_folder)
    if not create_temp_folder_is_exists:
        os.makedirs(create_temp_folder)
    return create_temp_folder + os.path.sep

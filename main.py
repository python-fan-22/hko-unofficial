import utility
from utility import take_input
import os
import getpass

username = getpass.getuser()


def loader():
    startup_message = "welcome to unofficial hk weather app v1. Please wait while the app loads."
    print(startup_message)

    installation_dir = r"C:Users\appdata\local\hko_unofficial"
    with open("file_index.txt") as file:
        file_list = [line.strip() for line in file.readlines()]
        file_dict = {file: os.path.exists(file) for file in file_list}
        has_settings = file_dict["settings.json"]
        has_file_index = file_dict["file_index.txt"]
        print(has_settings, has_file_index)
        if has_settings and has_file_index:
            loaded_files = True
        elif has_settings and not has_file_index:
            


def input_handler():
    print("enter a valid command")
    command = take_input()
    return command


loader()

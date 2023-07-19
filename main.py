import sys
import time

import utility
from utility import take_input
import os
import getpass
import requests
import installer

username = getpass.getuser()


def loader():
    startup_message = "welcome to unofficial hk weather app v1. Please wait while the app loads."
    print(startup_message)

    installation_dir = r"C:Users/{username}/appdata/local/hko_unofficial"
    if not os.path.exists(installation_dir):
        print("it looks like this is your first time using hko_unofficial. The installation will proceed shortly")
        installer.install()
        print("installation complete. Please rerun hko_unofficial :D")
        time.sleep(2)
        sys.exit()
    else:
        pass
    file_list = ["settings.json", "file_index.txt"]
    file_dict = {file: os.path.exists(file) for file in file_list}
    missing_files = []
    for file_name, exists in file_dict.items():
        if not exists:
            missing_files.append(file_name)
    for files in missing_files:
        downloaded_file = utility.download(files)
        with open(files, "w") as f:
            f.write(downloaded_file)


def input_handler():
    print("enter a valid command")
    command = take_input()
    return command


loader()

import utility
from utility import take_input
import os
import getpass
import requests

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
        elif has_settings == True and has_file_index == False:
            print("we couldn't find the file index. (this should never happen). would you like to try and download "
                  "the file index to your machine? (y/n)\n")
            wants_download_file_index = input(">")
            if wants_download_file_index == "y":
                content = utility.download("file_index.txt")
                with open("file_index.txt", "w") as file_index:
                    file_index.write(content)
            elif wants_download_file_index == "n":
                print("you can manually download the file at https://github.com/python-fan-22/api-caller/tree/main")
            else:
                print("error, something went quite wrong.")
        elif has_settings == False and has_file_index == True:
            print("we couldn't find the settings file. Would you like to try and download the default settings to "
                  "your machine? (y/n)\n")
            wants_download_settings = input(">")
            if wants_download_settings == "y":
                content = utility.download("settings.json")
                with open ("settings.json", "w") as file_settings:
                    file_settings.write(content)
            elif wants_download_settings == "n":
                print("you can manually download the settings file from the github repository and place it in the same directory as the app")
                print("the link can be found here, https://github.com/python-fan-22/api-caller/tree/main")
            else:
                print("error, something went quite wrong.")


def input_handler():
    print("enter a valid command")
    command = take_input()
    return command


loader()

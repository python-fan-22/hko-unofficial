import requests
import os
import getpass
import utility

username = getpass.getuser()
installation_dir = fr"C:Users/{username}/appdata/local/hko_unofficial"


def install():
    if os.path.exists(installation_dir):
        print(f"error, app installation already found at {installation_dir}.")
    else:
        pass
    print("downloading files...")
    file_list = [f"settings.json", f"file_index.txt"]
    for files in file_list:
        downloaded_file = utility.download(files)
        with open(files, "w") as f:
            f.write(downloaded_file)
    print("files downloaded successfully")



install()
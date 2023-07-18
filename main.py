import utility
from utility import take_input


def loader():
    startup_message = "welcome to unofficial hk weather app v1"
    print(startup_message)
    command = input_handler()
    if command == "ctemp":
        output = utility.current_temp()


def input_handler():
    print("enter a valid command")
    command = take_input()
    return command


loader()
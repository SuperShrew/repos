import os
import time
import json
from save_manager import *

def start():
    print("Welcome to dnd_game beta!")
    print("choose your option:")
    print("1. New Game")
    print("2. Load Game")
    print("3. Delete Save")
    print("4. Credits")
    print("5. Exit")
    opt = input("> ")
    match opt:
        case "1":
            create_save()
        case "2":
            load_save()
        case "3":
            del_save()
        case "4":
            os.system("clear")
            print("made by Clover")
            time.sleep(2)
            os.system("clear")
            start()
        case "5":
            print("bye.")
        case _:
            print("please pick a valid option\n")
            start()


start()

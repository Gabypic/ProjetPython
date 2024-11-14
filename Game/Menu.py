import os
import sys
import time
import clear
from Game import CreateGame as cg, Controls
from Musiques import MusicControl
from Database.DatabaseHandler import DatabaseHandler

DB = DatabaseHandler("Save.db")
def menu():
    MusicControl.music_controller("./Musiques/Ambiant/SkywardSwordMainMenu.mp3", False)
    print("\033[92mWELCOME ON Forest Escaper !\033[0m\n")
    print("--------------------------------")
    print("\033[94mMain Menu : \033[0m")
    print("1. Create New Game")
    print("2. Load Saved Game")
    print("3. About")
    print("4. Quit Game")
    print("-------------------------------")
    choice = input("Enter Your Choice: ")
    menu_selector(choice)


def menu_selector(choice):
    if choice == "1":
        print("\033[92mCreating Game... \033[0m")
        clear.clear_terminal(2)
        cg.create()

    elif choice == "2":
        print("\033[92mLoading Game... \033[0m")
        clear.clear_terminal(1)
        load_game()
        MusicControl.music_controller("./Musique/Ambiant/SkywardSwordMainMenu.mp3", True)

    elif choice == "3":
        print("\033[92mAbout... \033[0m")
        clear.clear_terminal(1)

    elif choice == "4":
        print("\033[91mReally want to quit ? \033[0m")
        validation = input('press enter to quit, insert "no" to return to menu : ')
        if validation == "no":
            print("\033[92mReturn to menu!\033[0m")
            clear.clear_terminal(1)
            menu()
        else:
            print("\033[91mQuitting Game... \033[0m")
            sys.exit()
    else:
        print("\033[91mInvalid Choice \n"
              "Reloading Menu...\033[0m")
        clear.clear_terminal(1)
        menu()


def load_game():
    player = DB.take_save(None)
    Controls.Controls_Menu(player)


def about():
    print("\03392mForest Escaper\033[0m is a level farming game.\n"
          "The objective is to reach level 21 to encounter the boss on the case 9,9."
          "By winning the boss fight, you reach the end of the game.")

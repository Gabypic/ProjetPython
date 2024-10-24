import os
import sys
import time
import clear
from Game import CreateGame as cg


def menu():
    print("\033[92mWELCOME ON PYTHON RPG PROJECT !\033[0m\n")
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

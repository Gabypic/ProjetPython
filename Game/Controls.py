from Musiques import MusicControl
from Game import EncounterMonster, Menu
from Database.DatabaseHandler import DatabaseHandler
import clear

DB = DatabaseHandler("Save.db")


def Controls_Menu(player):
    reload = True
    while True:
        clear.clear_terminal(0)
        if reload:
            MusicControl.music_controller(MusicControl.random_ambiant_song(), False)
        print("\n\033[92mControls\033[0m")
        print("---------------------------------------------------")
        print("\033[94mUp/Down/Left/Right\033[0m : go in the direction you want")
        print("\033[94mi\033[0m : Open inventory")
        print("\033[94me\033[0m : See equipped stuff")
        print("\033[94ms\033[0m : See your statistics")
        print("\033[94mr\033[0m : Game rules and informations")
        print("\033[93mSave\033[0m : Save game")
        print("\033[91mExit\033[0m : Quit game")
        print("---------------------------------------------------")
        choice = input("\nWhat do you want to do?\n").lower()
        reload = Controls_Selector(choice, player)


def Controls_Selector(selection, player):
    reload = False
    if selection == "up" or selection == "down" or selection == "left" or selection == "right":
        player.move(selection)
        ecounter = EncounterMonster.encounter_monster(player)
        print(player.place)
        if ecounter:
            reload = True
    if selection == "i":
        show_inventory(player)
    if selection == "e":
        show_equipped_weapon(player)
    if selection == "s":
        stats_printer(player)
    if selection == "r":
        rules_printer()
    if selection == "save":
        save(player)
    if selection == "exit":
        close_game()
    if selection == "cheat":
        level_choice = input("wich level do you want?\n")
        player.level = int(level_choice)
        player.place = [9, 9]
        player.attack = 2000
    return reload


def show_equipped_weapon(player):
    print(f"{player.equipped.name} --> damage : {player.equipped.damage}")
    input("\n\033[93mPress enter to continue\033[0m")
    return


def stats_printer(player):
    print("\033[94mYour informations :\033[0m\n"
          f"name : {player.name}\n"
          f"Difficulty : {player.difficulty}\n"
          f"Score : {player.score}\n"
          f"Level : {player.level}\n"
          f"experience : {player.experience}\n"
          f"health : {player.health}/{player.max_health}\n"
          f"defense : {player.defense}\n"
          f"attack : {player.attack}\n"
          f"speed: {player.speed}\n")
    input("\n\033[93mPress enter to continue\033[0m")
    return


def close_game():
    print("\033[91mDid you save the game ?\033[0m")
    choice = input("\nYes/No\n").lower()
    if choice == "no":
        print("Quitting whithout saving ?")
        choice = input("\n\033[93mYes/No\033[0m")
        if choice == "no":
            return
        if choice == "yes":
            print("\033[93mQuitting Game\033[0m")
            exit("Game closed")
        else:
            print("Incorrect Selection")
    if choice == "yes":
        print("\033[93mQuitting Game\033[0m")
        clear.clear_terminal(4)
        Menu.menu()


def show_inventory(player):
    player.show_inventory()
    input("\n\033[93mPress enter to continue\033[0m")
    return


def save(player):
    try:
        DB.delete_all()
        DB.add_save(player)
        DB.add_inventory(player)
        print("\033[92mSave Complete\033[0m")
        return
    except Exception as e:
        print(f"\033[91mSave Failed; {e}\033[0m")
        return


def rules_printer():
    clear.clear_terminal(1)
    print("Your objective is to reach level 21 et go to the 9,9 case to fight the boss\n"
          "On each movement, you have a chance to encounter a monster.\n"
          "By winning a fight, you will gain experience and have a chance to drop the mob weapon.\n"
          "After a win, you have a chance to found a chest on the case. "
          "There is a chance that there is nothing in the chest.\n"
          "To some levels, the monsters you will encounter will change and being stronger.\n"
          "The Mimic is a specific monster who will act like a chest by killing her.\n"
          "You still have a chance to cross a chest after killing a Mimic.\n"
          "Finally, the Boss is the strongest monster, his name is Nergigante the Forest Warden.\n"
          "\033[91mKill him to finish the game.\033\n[0m"
          "\033[94mGOOD LUCK\033[0m")
    input("\n\n\033[93mPress enter to continue\033[0m")
    return


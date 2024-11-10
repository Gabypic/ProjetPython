from Musiques import MusicControl
from Game import EncounterMonster


def Controls_Menu(player):
    song = MusicControl.music_controller(MusicControl.random_ambiant_song(), False)
    while True:
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
        Controls_Selector(choice, player)


def Controls_Selector(selection, player):
    if selection == "up" or selection == "down" or selection == "left" or selection == "right":
        player.move(selection)
        EncounterMonster.encounter_monster(player)
        print(player.place)
    if selection == "i":
        print("inventory")
    if selection == "e":
        print(player.equipped)
    if selection == "s":
        stats_printer(player)
    if selection == "r":
        print("rules")
    if selection == "save":
        print("save game")
    if selection == "exit":
        close_game()
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
        exit("Game closed")

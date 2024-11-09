import random
from Entity import Monsters, Weapons, Player
import clear
from Entity.Player import Player
from Game.MusicControl import music_controller


def fight(player, mob):
    turn = 1
    song = random_song()
    print(f"A {mob.name} attacks you, the fight begins\n")
    music_controller(song, False)
    while player.health > 0 and mob.health > 0:
        print(f"You are fighting against {mob.name}, hp : {mob.health}/{mob.max_health}, turn : {turn}\n"
              f"hp : {player.health}/{player.max_health}\n")
        print(f"You have three possibilities:\n"
              f"1. Attack\n"
              f"2. Open inventory\n"
              f"3. Flee\n\n")
        if mob.name == "Baby Goblin" or mob.name == "Nergigante":
            fight_choice(False, player, mob)
        else:
            fight_choice(True, player, mob)
        turn += 1
    music_controller(song, True)
    print("\033[92mCongratulations! You won the fight\033[0m")
    return


def fight_choice(is_escapable, player: Player, mob: Monsters):
    choice = input("What do you want to do? \n")
    if choice == "1":
        print(f"You attack the monster")
        player_damage = player.attack_monster(mob)
        print(f"You have inflected {player_damage}hp to the monster\n")
        if mob.health > 0:
            print('Monster attack you')
            mob_damage = mob.attack_player(player)
            print(f"Monster inflected you {mob_damage}hp\n")
        input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        return
    if choice == "2":
        print(f"Open inventory\n")
        input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        return
    if choice == "3":
        print(f"\033[93mBy fleeing, the monster present on the square,"
              f" as well as the potential items, will disappear. \n"
              f"You try to escape")
        if is_escapable:
            print("\033[92mEscape Success\033[0m")
        else:
            print("\033[91mYou can't escape against this monster\033[0m\n")
        input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        fight(player, mob)
    else:
        print("That's not a valid choice")
        return fight_choice(is_escapable, player, mob)


def random_song():
    songs = ["./Musiques/battle.mp3", "./Musiques/ChampionRed.mp3", "./Musiques/Cynthia.mp3", "./Musiques/Raikou.mp3",
             "./Musiques/ReshiramZekrom.pm3", "./Musiques/Suicune.mp3"]
    selected_song = random.choice(songs)
    return selected_song

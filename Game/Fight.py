import random
from Entity import Monsters
import clear
from Entity.Player import Player
from Musiques.MusicControl import music_controller
from Game import Loot, Controls, Menu


def fight(player: Player, mob: Monsters.Monsters):
    turn = 1
    if mob.name == "Nergigante":
        song = "./Musiques/Battle/Nergigante's Theme.mp3"
    else:
        song = random_battle_song()
    print(f"A {mob.name} attacks you, the fight begins\n")
    music_controller(song, False)
    while player.health > 0 and mob.health > 0:
        player.apply_active_effects()
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
    if player.health <= 0:
        print(f"\033[91mGAME OVER !\nYou lose against {mob.name}\nScore : {player.score}\033[0m")
        exit("\033[91mGame Over\033[0m")

    if mob.name != "Nergigante":
        print("\033[92mCongratulations! You won the fight\033[0m")
        print(f"You won {mob.experience_give}xp")

    else:
        print("\033[92mCongratulations! You finished the game !\033[0m")
        input("\n\033[93mPress enter to return home\033[0m")
        Menu.menu()

    Loot.Mob_Loot(player, mob)

    chest = random.randrange(1, 10)
    if chest >= 5:
        Loot.Chest_Loot(player, False)

    player.experience += mob.experience_give
    if player.experience < player.base_xp:
        print(f"{player.experience}/{player.base_xp}xp")
    else:
        player.level_up()
        print(f"well done you have leveled up. level:{player.level}")

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
        player.show_inventory()
        input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        return
    if choice == "3":
        print(f"\033[93mBy fleeing, the monster present on the square,"
              f" as well as the potential items, will disappear. \n"
              f"You try to escape")
        flee_chance = random.randrange(1, 10)
        if is_escapable and flee_chance > 2:
            print(f"You fled against {mob.name}")
            Controls.Controls_Menu(player)
        elif not is_escapable:
            print("\033[91mYou can't escape against this monster\033[0m\n")
            input("\n\033[93mPress enter to continue\033[0m")
        else:
            print("you didn't manage to escape")
            input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        fight(player, mob)
    else:
        print("That's not a valid choice")
        return fight_choice(is_escapable, player, mob)


def random_battle_song():
    songs = ["./Musiques/Battle/battle.mp3", "./Musiques/Battle/ChampionRed.mp3", "./Musiques/Battle/Cynthia.mp3",
             "./Musiques/Battle/Raikou.mp3", "./Musiques/Battle/ReshiramZekrom.mp3", "./Musiques/Battle/Suicune.mp3"]
    selected_song = random.choice(songs)
    return selected_song


def flee(player, mob):
    flee_chance = random.randrange(1, 10)
    if flee_chance > 2:
        print(f"You fled against {mob.name}")
        Controls.Controls_Menu(player)

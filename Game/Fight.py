from Entity import Monsters
import clear
from Entity.Player import Player

turn = 1


def fight(player, mob):
    while player.health > 0 or mob.health > 0:
        global turn
        if turn == 1:
            print(f"A {mob.name} attacks you, the fight begins\n")
        else:
            print(f"You are fighting against {mob.name}, hp : {mob.health}/{mob.max_health}, turn : {turn}\n\n")
        print(f"You have three possibilities:\n"
              f"1. Attack\n"
              f"2. Open inventory\n"
              f"3. Flee\n\n")
        if mob.name == "Baby Goblin":
            fight_choice(False, player, mob)
        else:
            fight_choice(True, player, mob)


def fight_choice(is_escapable, player, mob):
    global turn
    choice = input("What do you want to do? \n")
    if choice == "1":
        print(f"Attack\n")
        turn += 1
        input("\n\033[93mPress enter to continue\033[0m")
        clear.clear_terminal(0)
        return
    if choice == "2":
        print(f"Open inventory\n")
        turn += 1
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
        turn += 1
    else:
        print("That's not a valid choice")
        input("\n\033[93mPress enter to continue\033[0m\n")
        return fight_choice(is_escapable, player, mob)

def attack(player, mob):
    print("you are going to attack\n"
          "which weapon do you want to use ?")

    weapons = Player.inv

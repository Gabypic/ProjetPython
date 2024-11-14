import time

import clear
from Entity import Player
from Game import Beginning


def create():
    name = input("\033[94mWhat's your name : \033[0m")
    print(name)
    difficulty, base_xp = difficulty_selector()
    print(difficulty)
    print("\033[93mYour base stats will be randomly generated.\033[0m")
    player = Player.Player(name, 0, difficulty, 1, base_xp, 0,
                           0, 0, 0, 0, 0, {}, [4, 4], None)
    player.set_base_stats()
    print("\033[94mYour base stats :\033[0m\n"
          f"name : {player.name}\n"
          f"health : {player.health}\n"
          f"defense : {player.defense}\n"
          f"attack : {player.attack}\n"
          f"speed: {player.speed}\n")
    input("insert anything to start :")
    clear.clear_terminal(1)
    Beginning.begin(player)


def difficulty_selector():
    difficulty = input("\033[0mChoose the difficulty ? \033[0m (1 = easy, 2 = medium, 3 = hard \n"
                           "\033[93mDifficulty affects the experience needed to level up \033[0m \n"
                           "Difficulty : ")

    if difficulty == "1":
        print("\033[94mYou choose easy difficulty.\033[0m")
        return difficulty, 100
    elif difficulty == "2":
        print("\033[92mYou choose medium difficulty.\033[0m")
        return difficulty, 130
    elif difficulty == "3":
        print("\033[91mYou choose hard difficulty.\033[0m")
        return difficulty, 150
    elif difficulty == "":
        print("\033[91mPlease choose a difficulty level.\033[0m")
        return difficulty_selector()
    else:
        print("\033[91mYou choose too high difficulty!\033[0m")
        time.sleep(2)
        return difficulty_selector()

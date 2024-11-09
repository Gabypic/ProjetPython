import clear
from Entity import Monsters
from Game import Fight


def begin(player):
    print("You awaken in the midst of a forest, your mind a blank slate.\n"
          "As you gather your thoughts, you realize a dagger rests in its sheath at your belt\n"
          "and a leather satchel hangs empty by your side.\n"
          "After a few moments, you rise to your feet, determined to seek out help\n"
          "and uncover the mysteries of your situation and your identity.\n\n"
          "As you survey your surroundings, all you see is the endless expanse of trees.\n"
          "Your first goal is clear: find a way out of this forest.\n"
          "Just as you contemplate your escape, a faint crackling sound draws your attention from behind.\n"
          "You turn to find a small green creature watching you, a dagger clutched in its hand.\n"
          "Before you can react, it leaps at you with surprising speed.\n"
          "Instinctively, you draw your dagger and prepare to parry its strike.\n")

    baby_goblin = Monsters.Monsters("Punching Ball")

    input("\n\033[93mPress enter to start the fight...\033[0m")
    clear.clear_terminal(2)
    Fight.fight(player, baby_goblin)


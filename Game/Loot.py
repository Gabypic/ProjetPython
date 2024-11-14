from Entity import Weapons, items, Monsters, Player
import random


def Mob_Loot(player, mob):
    loot_chance = random.randint(1, 100)
    if loot_chance > 80 and mob.name != "Mimic" and mob.inventory:
        item = mob.inventory[0]
        if item in player.inventory:
            print("\033[93mYou already have this weapon, so you leave it on the ground\033[0m")
        else:
            player.inventory[item] = 1
    elif loot_chance > 15 and mob.name == "Mimic":
        print("By killing a Mimic, you obtain the item she was storing")
        Chest_Loot(player, True)
    else:
        print("\033[93mDuring the fight, the Monster weapon was damaged, so you cannot take it\033[0m")


def Chest_Loot(player: Player.Player, mimic):
    if not mimic:
        print("\033[93mThere is a little chest in the moss at the foot of a tree\033[0m")
    loot_chance = random.randint(1, 100)
    if loot_chance > 15 or mimic:
        item = items.random_item_drop()
        print(f"You found {item.name} in the chest")
        player.add_item(item, 1)
    else:
        print("\033[93mUnfortunately the chest was empty\033[0m")

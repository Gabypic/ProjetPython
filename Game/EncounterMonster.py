import random
from Entity import Monsters
from Game import Fight


def encounter_monster(player):
    monsters_by_level = {
        "low": ["Baby Goblin", "Slime", "Little Skeleton"],
        "medium": ["Mimic", "Goblin", "Skeleton"],
        "high": ["Giant Goblin", "Giant Skeleton", "Wolf"],
        "boss": ["Nergigante"]
    }

    if player.place == [9, 9] and player.level > 20:
        Fight.fight(player, Monsters.Monsters("Nergigante"))

    encounter_chance = random.randint(1, 10)
    possible_monsters = ""
    if encounter_chance > 3:
        if player.level < 7:
            possible_monsters = monsters_by_level["low"]
        elif 7 <= player.level < 15:
            possible_monsters = monsters_by_level["medium"]
        else:
            possible_monsters = monsters_by_level["high"]

        try:
            chosen_monster = random.choice(possible_monsters)
        except:
            chosen_monster = random.choice(monsters_by_level["boss"])

        Fight.fight(player, Monsters.Monsters(chosen_monster))
        return True

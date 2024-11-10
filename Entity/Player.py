from random import *
from Entity import Weapons, Monsters

class Player:
    def __init__(self, name, score, difficulty, level, base_xp, experience, health, defense, attack,
                 speed, inventory, place, equipped):
        self.name = name
        self.score = score
        self.difficulty = difficulty
        self.level = level
        self.base_xp = base_xp
        self.experience = experience
        self.health = health
        self.max_health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.inventory = inventory
        self.place = place
        self.equipped = equipped

    def __str__(self):
        return self.name

    def set_base_stats(self):
        self.health = randint(40, 60)
        self.max_health = self.health
        self.defense = randint(10, 20)
        self.attack = randint(12, 22)
        self.speed = randint(10, 20)
        self.equipped = Weapons.Dagger()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.base_xp = self.base_xp * 1.3
        self.max_health += randint(3, 7)
        self.health = self.max_health
        self.defense += randint(0, 4)
        self.attack += randint(0, 3)

    def take_damage(self, damage):
        self.health -= damage

    def attack_monster(self, mob):
        if self.equipped is not None:
            roll = randint(1, 10)
            if roll == 1:
                print("\033[91mYou missed the monster\033[0m")
                mob.take_damage(0)
                return 0
            if roll == 10:
                print("\033[92mBoom Critical Hit !\033[0m")
                damages = randint(self.attack - 1, self.attack + 4)
                if ((damages + self.equipped.damage) * 1.5) - mob.defense > 0:
                    mob.take_damage(((damages + self.equipped.damage) * 1.5) - mob.defense)
                    return (damages + self.equipped.damage) * 1.5
                else:
                    mob.take_damage(0)
                    return 0
            else:
                damages = randint(self.attack - 3, self.attack + 3)
                if (damages + self.equipped.damage) - mob.defense > 0:
                    mob.take_damage((damages + self.equipped.damage) - mob.defense)
                    return damages + self.equipped.damage - mob.defense
                else:
                    mob.take_damage(0)
                    return 0
        else:
            mob.take_damage(self.attack)
            return self.attack

    def move(self, direction):
        if direction == "up":
            if self.place[1] - 1 >= 0:
                self.place[1] -= 1
            else:
                print("\033[91mYou can't go higher, because of an enormous lake\033[0m")
        if direction == "down":
            if self.place[1] + 1 <= 9:
                self.place[1] += 1
            else:
                print("\033[91mYou can't go lower, because of a large ravine\033[0m")
        if direction == "left":
            if self.place[0] - 1 >= 0:
                self.place[0] -= 1
            else:
                print("\033[91mYou can't continue left, because of a big mountain\033[0m")
        if direction == "right":
            if self.place[0] + 1 <= 9:
                self.place[0] += 1
            else:
                print("\033[91mYou can't continue right, because of a mysterious and thick fog\033[0m")

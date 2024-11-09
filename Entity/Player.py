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
        self.health = randint(50, 80)
        self.max_health = self.health
        self.defense = randint(10, 20)
        self.attack = randint(12, 22)
        self.speed = randint(10, 20)
        self.equipped = Weapons.Dagger()

    def level_up(self):
        self.level += 1
        self.health += randint(3, 7)
        self.max_health = self.health
        attack_or_defense = randint(0, 1)
        if attack_or_defense:
            self.defense += randint(2, 5)
            self.attack += randint(1, 3)
        else:
            self.attack += randint(2, 5)
            self.defense += randint(1, 3)

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
                mob.take_damage((damages + self.equipped.damage) * 1.5)
                return (damages + self.equipped.damage) * 1.5
            else :
                damages = randint(self.attack - 3, self.attack + 3)
                mob.take_damage((damages + self.equipped.damage) - mob.defense)
                return damages + self.equipped.damage - mob.defense
        else:
            mob.take_damage(self.attack)
            return self.attack

    def move(self, direction):
        if direction == "up":
            self.place[1] -= 1
        if direction == "down":
            self.place[1] += 1
        if direction == "left":
            self.place[0] -= 1
        if direction == "right":
            self.place[0] += 1

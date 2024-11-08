from random import *
from Entity import Weapons, Monsters

class Player:
    def __init__(self, name, score, level, base_xp, experience, health, defense, attack,
                 speed, inventory, place, equipped):
        self.name = name
        self.score = score
        self.level = level
        self.base_xp = base_xp
        self.experience = experience
        self.health = health
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
        self.defense = randint(10, 20)
        self.attack = randint(12, 22)
        self.speed = randint(10, 20)
        self.equipped = Weapons.Dagger()

    def level_up(self):
        self.level += 1
        self.health += randint(3, 7)
        attack_or_defense = randint(0, 1)
        if attack_or_defense:
            self.defense += randint(2, 5)
            self.attack += randint(1, 3)
        else:
            self.attack += randint(2, 5)
            self.defense += randint(1, 3)

    def attack_monster(self, mob):
        if self.equipped is not None:
            mob.take_damage(self.attack + self.equipped.damage)
        else:
            mob.take_damage(self.attack)

from random import *


class Entity:
    def __init__(self, name, level, experience_give, health, defense, attack, speed, inventory, place, equipped):
        self.name = name
        self.level = level
        self.experience_give = experience_give
        self.health = health
        self.max_health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.inventory = inventory
        self.place = place
        self.equipped = equipped

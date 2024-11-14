from random import *
from Entity import Weapons, Monsters, items


class Player:
    def __init__(self, name, score, difficulty, level, base_xp, experience, health, max_health, defense, attack,
                 speed, inventory, place, equipped):
        self.name = name
        self.score = score
        self.difficulty = difficulty
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
        if max_health == 0:
            self.max_health = health
        else:
            self.max_health = max_health
        self.active_effects = []

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
        self.max_health += randint(2, 4)
        self.health = self.max_health
        self.defense += randint(0, 3)
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

    def add_item(self, item, quantity):
        if isinstance(item, Weapons.Weapons) and (self.equipped and self.equipped.name == item.name or item in self.inventory):
            print(f"You already have a {item.name}.")
            return

        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def use_item(self, item):
        if item in self.inventory:
            self.inventory[item] -= 1

    def show_inventory(self):
        print("\033[94mInventory:\033[0m")
        inventory_items = list(self.inventory.keys())

        for index, item in enumerate(inventory_items):
            print(f"{index + 1}. {item.name} x{self.inventory[item]}")

        choice = input("\nSelect an item to use or equip (number), or press 'q' to exit:\n").lower()
        if choice == 'q':
            return

        try:
            item_index = int(choice) - 1
            selected_item = inventory_items[item_index]

            if isinstance(selected_item, Weapons.Weapons):
                self.equip_weapon(selected_item)
            elif isinstance(selected_item, items.Items):
                selected_item.apply_effects(self)
                self.use_item(selected_item)

        except (IndexError, ValueError):
            print("\033[91mInvalid selection\033[0m")

    def equip_weapon(self, new_weapon):
        if self.equipped:
            if self.equipped in self.inventory:
                self.inventory[self.equipped] += 1
            else:
                self.inventory[self.equipped] = 1

        self.equipped = new_weapon
        print(f"\033[92mEquipped {new_weapon.name}\033[0m")

        if self.inventory[new_weapon] > 1:
            self.inventory[new_weapon] -= 1
        else:
            del self.inventory[new_weapon]

    def apply_active_effects(self):
        for effect in self.active_effects[:]:
            if effect['turns'] > 0:
                effect['apply'](self)
                effect['turns'] -= 1
            else:
                self.active_effects.remove(effect)
                effect['remove'](self)

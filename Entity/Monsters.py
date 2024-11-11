from Entity import GlobalEntity, Weapons
import random


class Monsters(GlobalEntity.Entity):
    def __init__(self, name):

        if name == "Baby Goblin":
            super().__init__(name, 1, 200, 30, 5,
                             5, 12, [Weapons.Dagger()], None, Weapons.Dagger())
        if name == "Slime":
            super().__init__(name, 2, 200, 45, 8,
                             16, 14, [], None, None)
        if name == "Goblin":
            super().__init__(name, 5, 600, 60, 23,
                             25, 15, [Weapons.Sword()], None, Weapons.Sword())
        if name == "Giant Goblin":
            super().__init__(name, 15, 900, 90, 27,
                         32, 20, [Weapons.Axe()], None, Weapons.Axe())
        if name == "Little Skeleton":
            super().__init__(name, 2, 300, 50, 10,
                             18, 14, [Weapons.Rapier()], None, Weapons.Rapier())
        if name == "Skeleton":
            super().__init__(name, 6, 650, 65, 12,
                             22, 20, [Weapons.Sword()], None, Weapons.Sword())
        if name == "Giant Skeleton":
            super().__init__(name, 15, 1000, 100, 30,
                             35, 20, [Weapons.LongSword()], None, Weapons.LongSword())
        if name == "Wolf":
            super().__init__(name, 17, 1100, 90, 35,
                             42, 30, [], None, None)
        if name == "Punching Ball":
            super().__init__(name, 1, 0, 9999, 0,
                             0, 0, [], None, None)
        if name == "Mimic":
            super().__init__(name, 10, 550, 75, 24,
                             30, 14, [], None, None)
        if name == "Nergigante":
            super().__init__(name, 25, 5000, 250, 42,
                             50, 100, [],  [9, 9], None)

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        if self.equipped is not None:
            roll = random.randint(1, 20)
            if roll == 1:
                print("\033[92mMonster missed you\033[0m")
                player.take_damage(0)
                return 0
            if roll == 20:
                print("\033[91mMonster Critically hit you\033[0m")
                if ((self.attack + self.equipped.damage) * 2) - player.defense > 0:
                    player.take_damage(((self.attack + self.equipped.damage) * 2) - player.defense)
                    return ((self.attack + self.equipped.damage) * 2) - player.defense
                else:
                    player.take_damage(0)
                    return 0
            else:
                damage = random.randint(self.attack - 5, self.attack + 2)
                if (damage + self.equipped.damage) - player.defense > 0:
                    player.take_damage((damage + self.equipped.damage) - player.defense)
                    return (damage + self.equipped.damage) - player.defense
                else:
                    player.take_damage(0)
                    return 0
        else:
            if self.attack - player.defense > 0:
                player.take_damage(self.attack - player.defense)
                return self.attack - player.defense
            else:
                player.take_damage(0)
                return 0

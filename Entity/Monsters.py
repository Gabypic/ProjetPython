from Entity import GlobalEntity, Weapons
import random


class Monsters(GlobalEntity.Entity):
    def __init__(self, name):

        if name == "Baby Goblin":
            super().__init__(name, 1, 200, 30, 5,
                             5, 12, [], None, Weapons.Dagger())
        if name == "Punching Ball":
            super().__init__(name, 1, 0, 9999, 0,
                             0, 0, [], None, None)
        if name == "Mimmic":
            super().__init__(name, 1, 400, 50, 10,
                             11, 14, [], None, None)
        if name == "Nergigante":
            super().__init__(name, 25, 5000, 500, 42,
                             69, 100, [],  [9, 9], None)

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
                player.take_damage((self.attack + self.equipped.damage) * 2)
                return (self.attack + self.equipped.damage) * 2
            else:
                damage = random.randint(self.attack - 5, self.attack + 2)
                player.take_damage(damage + self.equipped.damage)
                return damage + self.equipped.damage
        else:
            player.take_damage(self.attack)
            return self.attack

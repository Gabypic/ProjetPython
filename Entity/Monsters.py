from Entity import GlobalEntity, Weapons


class Monsters(GlobalEntity.Entity):
    def __init__(self, name):

        if name == "Baby Goblin":
            super().__init__(name, 1, 200, 25, 5,
                             8, 12, [], None, Weapons.Dagger)
        if name == "Nergigante":
            super().__init__(name, 25, 5000, 500, 42,
                             69, 100, [],  [9, 9], None)
    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        if self.equipped is not None:
            player.take_damage(self.attack + self.equipped.damage)
        else:
            player.take_damage(self.attack)
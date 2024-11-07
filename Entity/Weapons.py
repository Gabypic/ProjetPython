from Entity import GlobalItems, Player, GlobalEntity, Monsters


class Weapons(GlobalItems.Items):
    def __init__(self, name, damage, protection, speed):
        super().__init__(name, 0, 0, 0)
        self.name = name


class Dagger(Weapons):
    def __init__(self):
        super().__init__("Dagger", 5, 0, 0)

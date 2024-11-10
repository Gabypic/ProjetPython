from Entity import GlobalItems, Player, GlobalEntity, Monsters


class Weapons(GlobalItems.Items):
    def __init__(self, name, damage=0, protection=0, speed=0, heal=0, duration=0):
        super().__init__(name, damage, protection, speed, heal, duration)


class Dagger(Weapons):
    def __init__(self):
        super().__init__("Dagger", damage=5, speed=6)


class Sword(Weapons):
    def __init__(self):
        super().__init__("Sword", damage=10, speed=4)


class LongSword(Weapons):
    def __init__(self):
        super().__init__("Long Sword", damage=13, speed=2)


class Rapier(Weapons):
    def __init__(self):
        super().__init__("Rapier", damage=8, speed=8)


class Axe(Weapons):
    def __init__(self):
        super().__init__("Axe", damage=15, speed=1)


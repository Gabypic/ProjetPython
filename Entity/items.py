import random
from Entity import GlobalItems


class Items(GlobalItems.Items):
    def __init__(self, name, damage=0, protection=0, speed=0, heal=0, duration=0):
        super().__init__(name, damage, protection, speed, heal, duration)


class SmallHealPotion(Items):
    def __init__(self):
        super().__init__("Small Heal Potion", heal=20)


class MediumHealPotion(Items):
    def __init__(self):
        super().__init__("Medium Heal Potion", heal=40)


class LargeHealPotion(Items):
    def __init__(self):
        super().__init__("Large Heal Potion", heal=70)


class ProtectionRune(Items):
    def __init__(self):
        super().__init__("Protection Rune", protection=12, duration=5)


class SpeedCard(Items):
    def __init__(self):
        super().__init__("Speed Card", speed=10, duration=5)


class PopeiSpinach(Items):
    def __init__(self):
        super().__init__("Popei Spinach", damage=15, duration=5)


table_rarete = {
    SmallHealPotion(): 20,
    MediumHealPotion(): 10,
    LargeHealPotion(): 2,
    ProtectionRune(): 10,
    SpeedCard(): 10,
    PopeiSpinach(): 10
}


def random_item_drop():
    items = list(table_rarete.keys())
    rarity = list(table_rarete.values())
    selected_item = random.choices(items, weights=rarity, k=1)[0]
    return selected_item


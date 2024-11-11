import random
from Entity import GlobalItems


class Items(GlobalItems.Items):
    def __init__(self, name, damage=0, protection=0, speed=0, heal=0, duration=0):
        super().__init__(name, damage, protection, speed, heal, duration)

    def apply_effects(self, player):
        if self.heal > 0:
            player.health = min(player.health + self.heal, player.max_health)
            print(f"{player.name} a récupéré {self.heal} points de vie. Vie actuelle : {player.health}/{player.max_health}")
        if self.protection > 0:
            player.defense += self.protection
            print(f"{player.name} a augmenté sa défense de {self.protection} pour {self.duration} tours.")
        if self.speed > 0:
            player.speed += self.speed
            print(f"{player.name} a augmenté sa vitesse de {self.speed} pour {self.duration} tours.")
        if self.damage > 0:
            player.attack += self.damage
            print(f"{player.name} a augmenté son attaque de {self.damage} pour {self.duration} tours.")


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
        super().__init__("Protection Rune", protection=9, duration=5)


class SpeedCard(Items):
    def __init__(self):
        super().__init__("Speed Card", speed=10, duration=5)


class PopeiSpinach(Items):
    def __init__(self):
        super().__init__("Popei Spinach", damage=10, duration=5)


rarity_table = {
    SmallHealPotion(): 50,
    MediumHealPotion(): 30,
    LargeHealPotion(): 10,
    ProtectionRune(): 5,
    SpeedCard(): 0,
    PopeiSpinach(): 5
}


def random_item_drop():
    items = list(rarity_table.keys())
    rarity = list(rarity_table.values())
    selected_item = random.choices(items, weights=rarity, k=1)[0]
    return selected_item


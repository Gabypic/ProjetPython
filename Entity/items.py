import random
from Entity import GlobalItems


class Items(GlobalItems.Items):
    def __init__(self, name, damage=0, protection=0, speed=0, heal=0, duration=0):
        super().__init__(name, damage, protection, speed, heal, duration)

    def apply_effects(self, player):
        if self.heal > 0:
            player.health = min(player.health + self.heal, player.max_health)
            print(
                f"{player.name} has recovered {self.heal} health points. Current health: {player.health}/{player.max_health}")

        if self.protection > 0:
            player.active_effects.append({
                'apply': lambda p: p.defense + self.protection,
                'remove': lambda p: p.defense - self.protection,
                'turns': self.duration
            })
            print(f"{player.name} increased their defense by {self.protection} for {self.duration} turns.")

        if self.speed > 0:
            player.active_effects.append({
                'apply': lambda p: p.speed + self.speed,
                'remove': lambda p: p.speed - self.speed,
                'turns': self.duration
            })
            print(f"{player.name} increased their speed by {self.speed} for {self.duration} turns.")

        if self.damage > 0:
            player.active_effects.append({
                'apply': lambda p: p.attack + self.damage,
                'remove': lambda p: p.attack - self.damage,
                'turns': self.duration
            })
            print(f"{player.name} increased their attack by {self.damage} for {self.duration} turns.")


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
    ProtectionRune(): 10,
    SpeedCard(): 0,
    PopeiSpinach(): 10
}


def random_item_drop():
    items = list(rarity_table.keys())
    rarity = list(rarity_table.values())
    selected_item = random.choices(items, weights=rarity, k=1)[0]
    return selected_item


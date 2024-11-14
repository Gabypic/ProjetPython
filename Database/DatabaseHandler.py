import os
import sqlite3
from Entity import Weapons, items, Player

item_classes = {
    "Dagger": Weapons.Dagger,
    "Sword": Weapons.Sword,
    "LongSword": Weapons.LongSword,
    "Rapier": Weapons.Rapier,
    "Axe": Weapons.Axe,
    "Small Heal Potion": items.SmallHealPotion,
    "Medium Heal Potion": items.MediumHealPotion,
    "Large Heal Potion": items.LargeHealPotion,
    "Protection Rune": items.ProtectionRune,
    "Speed Card": items.SpeedCard,
    "Popei Spinach": items.PopeiSpinach
}


class DatabaseHandler:
    def __init__(self, database_name: str):
        self.connect = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.connect.row_factory = sqlite3.Row

    def add_save(self, player):
        cursor = self.connect.cursor()
        query = (f"INSERT INTO PlayerSave (name, score, difficulty, level, base_xp, xp,"
                 f" health, max_health, defense, attack, speed, placeX, placeY, equipped)"
                 f" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
        cursor.execute(query, (player.name, player.score, player.difficulty, player.level, player.base_xp,
                               player.experience, player.health, player.max_health, player.defense, player.attack,
                               player.speed,
                               player.place[0], player.place[1], player.equipped.name,))
        cursor.close()
        self.connect.commit()

    def add_inventory(self, player):
        cursor = self.connect.cursor()
        query = "INSERT INTO Inventory (item, quantity) VALUES (?, ?);"
        for item, quantity in player.inventory.items():
            cursor.execute(query, (item.name, quantity))
        self.connect.commit()
        cursor.close()

    def delete_all(self):
        cursor = self.connect.cursor()
        query = "DELETE FROM Inventory;"
        cursor.execute(query)
        query = "DELETE FROM PlayerSave;"
        cursor.execute(query)
        cursor.close()
        self.connect.commit()

    def take_save(self, player=None):
        global item_classes

        cursor = self.connect.cursor()
        cursor.execute("SELECT * FROM PlayerSave LIMIT 1;")
        player_data = cursor.fetchone()

        if player_data:
            name = player_data["name"]
            score = player_data["score"]
            difficulty = player_data["difficulty"]
            level = player_data["level"]
            base_xp = player_data["base_xp"]
            experience = player_data["xp"]
            health = player_data["health"]
            max_health = player_data["max_health"]
            defense = player_data["defense"]
            attack = player_data["attack"]
            speed = player_data["speed"]
            place = [player_data["placeX"], player_data["placeY"]]
            equipped_name = player_data["equipped"]
            equipped = item_classes.get(equipped_name, None)() if equipped_name in item_classes else None

            player = Player.Player(name, score, difficulty, level, base_xp, experience, health, max_health, defense,
                                   attack, speed, {}, place, equipped)

            cursor.execute("SELECT * FROM Inventory;")
            inventory_data = cursor.fetchall()

            for item_data in inventory_data:
                item_name = item_data["item"]
                quantity = item_data["quantity"]

                if item_name in item_classes:
                    item_instance = item_classes[item_name]()
                    player.inventory[item_instance] = quantity

        cursor.close()
        return player

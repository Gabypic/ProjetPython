from Entity import GlobalEntity


class Monster(GlobalEntity.Entity):
    def __init__(self, name, level, experience_give, health, defense, attack, speed, inventory):
        super().__init__(name, level, experience_give, health, defense, attack, speed, inventory)

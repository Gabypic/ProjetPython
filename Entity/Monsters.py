from Entity import GlobalEntity


class Monster(GlobalEntity.Entity):
    def __init__(self, name):

        if name == "Baby Goblin":
            super().__init__(name, 1, 200, 25, 5, 8, 12, [])

from Entity import GlobalItems, Player, GlobalEntity, Monsters


class Weapons(GlobalItems.Items):
    def __init__(self, name):
        super().__init__(name, 0, 0, 0, 0)
        self.name = name


class Dagger:
    def use(self, user):

        user.attack += 5
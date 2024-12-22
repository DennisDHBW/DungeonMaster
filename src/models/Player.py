class Player:

    MAX_HEALTH = 100

    def __init__(self, name: str, strength: float):
        self.__name = name
        self.__health = self.MAX_HEALTH
        self.__strength = strength

    def __str__(self):
        print(f"Player {self.name} has {self.__strength} strength and {self.__health} health.")

    def take_damage(self, damage: float):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def regain_health(self, health_regain: float):
        self.__health += health_regain
        if self.__health > self.MAX_HEALTH:
            self.__health = self.MAX_HEALTH

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    @name.setter
    def name(self, name):
        raise AttributeError()

    @strength.setter
    def strength(self, strength):
        raise AttributeError()

    @health.setter
    def health(self, health):
        raise AttributeError()
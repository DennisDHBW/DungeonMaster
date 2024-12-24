class Monster:

    def __init__(self, name: str, strength: int, health: int):
        self.__name = name
        self.__strength = strength
        self.__health = health
        self.__healthInit = health

    def __str__(self):
        return f"Monster {self.__name} has {self.__strength} strength and {self.__health} health."

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    @property
    def lost_health(self): #unexpected
        return self.__healthInit - self.__health

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0


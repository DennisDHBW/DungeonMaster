class Monster:

    def __init__(self, name: str, strength: int, health: int):
        self.__name = name
        self.__strength = strength
        self.__health = health

    def __str__(self):
        print(f"Monster {self.__name} has {self.__strength} strength and {self.__health} health.")

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
class Player:

    # konstante mit maximalen spielerlebenspunkten
    MAX_HEALTH = 100

    # initialisierung des objekts mit privaten instanzvariablen
    def __init__(self, name: str, strength: int):
        self.__name = name
        self.__health = self.MAX_HEALTH
        self.__strength = strength

    # objekt string - wenn ein objekt der klasse player geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben
    def __str__(self):
        return f"Player {self.name} has {self.__strength} strength and {self.__health} health."

    # getter fuer die privaten instanzvariablen
    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    # objekt funktion um das leben des spielers zu reduzieren
    def take_damage(self, damage: int):
        self.__health -= int(damage)
        if self.__health < 0:
            self.__health = 0

    # objekt funktion um das leben des spielers zu erhoehen
    def regain_health(self, health_regain: int):
        self.__health += int(health_regain)
        if self.__health > self.MAX_HEALTH:
            self.__health = self.MAX_HEALTH

class Monster:

    # initialisierung des objekts mit privaten instanzvariablen
    def __init__(self, name: str, strength: int, health: int):
        self.__name = name
        self.__strength = strength
        self.__health = health
        self.__healthInit = health

    # objekt string - wenn ein objekt der klasse monster geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben
    def __str__(self):
        return f"Monster {self.__name} has {self.__strength} strength and {self.__health} health."

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

    @property
    def lost_health(self): #unexpected
        return self.__healthInit - self.__health

    # objekt funktion um das leben des monsters zu reduzieren
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0


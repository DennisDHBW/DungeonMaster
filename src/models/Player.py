class Player:

    # konstante mit maximalen spielerlebenspunkten
    MAX_HEALTH = 100

    # initialisierung des objekts mit privaten instanzvariablen (konstruktor: name als string und strength als integer)
    def __init__(self, name: str, strength: int): # konstruktur beinhaltet erforderliche angaben bei initialisierung einer objektinstanz
        self.__name = name # private instanzvariable __name erhaelt den bei der initialisierung uebergebenen wert (gespeichert in variable "name" vom typ string)
        self.__health = self.MAX_HEALTH # private instanzvariable __health erhaelt den wert der konstanten variable MAX_HEALTH
        self.__strength = strength # private instanzvariable __strength erhaelt den bei der initialisierung uebergebenen wert (gespeichert in variable "strength" vom typ int)

    # objekt-string - wenn eine objektinstanz der klasse player geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben (mit spielername, spieler staerke, spielerleben)
    def __str__(self):
        return f"Player {self.name} has {self.__strength} strength and {self.__health} health."

    # definition einer getter methode (@property) mit dem namen "name" fuer die private instanzvariable __name
    @property
    def name(self):
        return self.__name # rueckgabe des wertes, der in der privaten instanzvariable __name gespeichert ist

    # definition einer getter methode (@property) mit dem namen "health" fuer die private instanzvariable __health
    @property
    def health(self):
        return self.__health # rueckgabe des wertes, der in der privaten instanzvariable __health gespeichert ist

    # definition einer getter methode (@property) mit dem namen "strength" fuer die private instanzvariable __strength
    @property
    def strength(self):
        return self.__strength # rueckgabe des wertes, der in der privaten instanzvariable __strength gespeichert ist

    # methode um das leben des spielers zu reduzieren
    def take_damage(self, damage: int):
        self.__health -= int(damage) # private instanzvariable __health wird um den wert der integer variable "damage" reduziert
        if self.__health < 0: # falls wert von __health kleiner als 0 ist dann...
            self.__health = 0 # ... setze den wert auf 0

    # methode um das leben des spielers zu erhoehen
    def regain_health(self, health_regain: int):
        self.__health += int(health_regain) # private instanzvariable __health wird um den wert der integer variable "health_regain" erhoeht
        if self.__health > self.MAX_HEALTH: # falls wert von __health groesser als variable der klasse MAX_HEALTH ist dann...
            self.__health = self.MAX_HEALTH # ... wird der wert der privaten instanzvariable auf den wert der klassenvariable MAX_HEALTH gesetzt

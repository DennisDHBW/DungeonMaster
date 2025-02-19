class Monster:

    # initialisierung der objektinstanz mit privaten instanzvariablen
    def __init__(self, name: str, strength: int, health: int):
        self.__name = name # initialisierung der privaten instanzvariable __name mit dem im konstruktur uebergebenen wert (gespeichert in name)
        self.__strength = strength # initialisierung der privaten instanzvariable __strength mit dem im konstruktur uebergebenen wert (gespeichert in strength)
        self.__health = health # initialisierung der privaten instanzvariable __health mit dem im konstruktur uebergebenen wert (gespeichert in health)
        self.__healthInit = health # initialisierung der privaten instanzvariable __healthInit mit dem im konstruktur uebergebenen wert (gespeichert in health) fuer "lost_health" funktion

    # objekt string - wenn eine objektinstanz der klasse monster geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben
    def __str__(self):
        return f"Monster {self.__name} has {self.__strength} strength and {self.__health} health."

    # definierung einer getter methode (@property) mit dem namen "name" fuer die private instanzvariable __name
    @property
    def name(self):
        return self.__name

    # definierung einer getter methode (@property) mit dem namen "health" fuer die private instanzvariable __health
    @property
    def health(self):
        return self.__health

    # definierung einer getter methode (@property) mit dem namen "strength" fuer die private instanzvariable __strength
    @property
    def strength(self):
        return self.__strength

    # definierung einer getter methode (@property) mit dem namen "lost_health" fuer die berechnung des erlittenen schaden
    # durch das subtrahieren der privaten instanzvariable __health von der private instanzvariable __healthInit
    @property
    def lost_health(self):
        return self.__healthInit - self.__health

    # methode um das leben des monsters zu reduzieren
    def take_damage(self, damage):
        self.__health -= damage # private instanzvariable __health wird um den wert der im konstruktur uebergebenen variable "damage" verringert
        if self.__health < 0: # falls der wert der privaten instanzvariable __health kleiner als 0 geworden ist ...
            self.__health = 0 # setze den wert der privaten instanzvariable __health auf 0


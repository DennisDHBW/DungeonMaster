from src.models.Player import Player
from src.models.Monster import Monster

class Room:

    # initialisierung des objekts mit privaten instanzvariablen
    def __init__(self, description, monster: Monster):
        self.__description = description # initialisierung der privaten instanzvariable __description mit dem im konstruktur uebergebenen wert (gespeichert in description)
        self.__monster = monster # initialisierung der privaten instanzvariable __monster mit dem im konstruktur uebergebenen objektinstanz monster

    # objekt-string - wenn eine objektinstanz der klasse room geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben (raumbeschreibung)
    def __str__(self):
        return str(self.__description) # rueckgabe des strings, welcher in der privaten instanzvariable __description steht

    # definition einer getter methode (@property) mit dem namen "description" fuer die private instanzvariable __description
    @property
    def description(self):
        return self.__description

    # definition einer getter methode (@property) mit dem namen "monster" fuer die private instanzvariable __monster
    @property
    def monster(self):
        return self.__monster

    # methode damit der spieler eine runde mit dem monster des raumes
    # kaempfen kann. ablauf: monsterangriff (+auswirkungen) dann Spielerangriff (+auswirkungen)
    def fight_round(self, player: Player):

        monster = self.monster

        # angriff des monsters
        print(f"The monster hits you with {monster.strength} strength.") # konsolenausgabe basierend auf staerke des monsters
        player.take_damage(monster.strength) # aufruf der funktion "take_damage" der objektinstanz player mit dem wert der getter methode strength der objektinstanz monster

        # auswirkungen des angriffs des monsters
        print(player) # aufruf der funktion __str__ der objektinstanz player
        if player.health <= 0: # falls der zurueckgegebene wert der getter methode health der objektinstanz player kleiner gleich 0 dann ...
            print("You lost the fight") # ... konsolenausgabe mit dem entsprechenden text
            return # ... und rueckgabe/"abbruch" der funktion

        # angriff des spielers
        print(f"You hit the monster with {player.strength} strength.") # konsolenausgabe basierend auf staerke des spielers
        monster.take_damage(player.strength) # aufruf der funktion "take_damage" der objektinstanz monster mit dem zurueckgegebenen wert der getter methode strength der objektinstanz player

        # auswirkungen des angriffs des spielers
        if monster.health <= 0: # wenn zurueckgegebene wert der getter methode health der objektinstanz monster kleiner gleich 0 dann ...
            print("The monster is dead") # konsolen ausgabe
            regain_health = int(monster.lost_health / 2) # ... variable mit zurueckgegebenen wert der getter methode lost_health der objektinstanz monster durch 2 geteilt und als int gespeichert
            player.regain_health(regain_health) # ... und aufruf der funktion "regain_health" der objektinstanz player mit dem wert der integer variable regain_health
            print(f"Player {player.name}, you regained health: {player.health}") # ... und konsolenausgabe basierend auf spieler name und verbleibendes spielerleben
        else: # falls nicht...
            print(monster) # konsolen ausgabe der funktion __str__ der objektinstanz monster

    # methode damit der spieler mit dem raum interagieren kann.
    # moeglichkeiten: fluechten oder kaempfen
    def interact(self, player: Player):

        monster = self.monster # initiierung der variable monster mit der im dictionary gespeicherten objektinstanz vom typ monster

        print(f"Welcome to the {self.description}") # konsolenausgabe basierend auf raumbeschreibung
        print(f"The monster {monster.name} appears!") # konsolenausgabe basierend auf name des monsters

        while monster.health > 0 and player.health > 0: # schleife sollange monster und spieler leben (health groesser 0)
            action = input("Would you like to run (r) or fight (f)?") # variable action mit benutzereingabe befuellen (string)
            match action.lower(): # string formatieren (kleinbuchstaben)
                case "r" | "run": # falls "r" oder "run" eingegeben wurde ...
                    print("You chose RUN!") # ... konsolenausgabe
                    player.take_damage(10) # ... und aufruf der funktion take_damage der objektinstanz player mit dem wert 10
                    print("You sprint out of the room and take 10 damage!") # ... und konsolenausgabe
                    print(player) # ... ausgabe des spielerobjektes
                    break # ... und brich den schleifendurchlauf ab
                case "f" | "fight": # falls "f" oder "fight" eingegeben wurde ...
                    print("You chose FIGHT!") # ... konsolenausgabe
                    self.fight_round(player) # aufruf der funktion fight_round mit der objektinstanz player
                case _: # bei nicht definierten faellen (falls die ersten beiden faelle nicht matchen) ...
                    print(f"[{action}] is an invalid action.") # ...konsolenausgabe

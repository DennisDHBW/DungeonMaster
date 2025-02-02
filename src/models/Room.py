from src.models.Player import Player
from src.models.Monster import Monster

class Room:

    # initialisierung des objekts mit privaten instanzvariablen
    def __init__(self, description, monster: Monster):
        self.__description = description
        self.__monster = monster

    # objekt string - wenn eine objektinstanz der klasse room geprintet wird, dann
    # wird der nachfolgende string zurueckgegeben (raumbeschreibung)
    def __str__(self):
        return str(self.__description)

    # getter fuer die privaten instanzvariablen
    @property
    def description(self):
        return self.__description

    @property
    def monster(self):
        return self.__monster

    # methode damit der spieler eine runde mit dem monster des raumes
    # kaempfen kann. ablauf: monsterangriff (+auswirkungen) dann Spielerangriff (+auswirkungen)
    def fight_round(self, player: Player):

        monster = self.monster

        # angriff des monsters
        print(f"The monster hits you with {monster.strength} strength.")
        player.take_damage(monster.strength)

        # auswirkungen des angriffs des monsters
        print(player)
        if player.health <= 0:
            print("You lost the fight")
            return

        # angriff des spielers
        print(f"You hit the monster with {player.strength} strength.")
        monster.take_damage(player.strength)

        # auswirkungen des angriffs des spielers
        if monster.health <= 0:
            print("The monster is dead")
            regain_health = int(monster.lost_health / 2)
            player.regain_health(regain_health)
            print(f"Player {player.name}, you regained health: {player.health}")
        else:
            print(monster)

    # methode damit der spieler mit dem raum interagieren kann.
    # moeglichkeiten: fluechten oder kaempfen
    def interact(self, player: Player):

        monster = self.monster

        print(f"Welcome to the {self.description}")
        print(f"The monster {monster.name} appears!")

        while monster.health > 0 and player.health > 0:
            action = input("Would you like to run (r) or fight (f)?")
            match action.lower():
                case "r" | "run":
                    print("You chose RUN!")
                    player.take_damage(10)
                    print("You sprint out of the room and take 10 damage!")
                    break
                case "f" | "fight":
                    print("You chose FIGHT!")
                    self.fight_round(player)
                case _:
                    print(f"[{action}] is an invalid action.")

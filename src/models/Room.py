from src.models.Player import Player
from src.models.Monster import Monster

class Room:

    def __init__(self, description, monster: Monster):
        self.__description = description
        self.__monster = monster

    def __str__(self):
        return str(self.__description)

    @property
    def description(self):
        return self.__description

    @property
    def monster(self):
        return self.__monster

    def fight_round(self, player: Player):

        monster = self.monster

        # attack: monster
        print(f"The monster hits you with {monster.strength} strength.")
        player.take_damage(monster.strength)

        # impact - attack: monster
        print(player)
        if player.health <= 0:
            print("You lost the fight")
            return

        # attack: player
        print(f"You hit the monster with {player.strength} strength.")
        monster.take_damage(player.strength)

        # impact - attack: player
        if monster.health <= 0:
            print("The monster is dead")
            regain_health = int(monster.lost_health / 2)
            player.regain_health(regain_health)
            print(f"Player {player.name}, you regained health: {player.health}")
        else:
            print(monster)

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

from src.models.Player import Player
from src.models.Monster import Monster

class Room:

    def __init__(self, description, monster: Monster):
        self.__description = description
        self.__monster = monster

    def __str__(self):
        print(self.__description)


    def interact(self, player: Player):
        print(f"Welcome to the {self.__description}")
        "# TODO"

    def fight_round(self, player: Player):
        monster = self.__monster

        while monster.health > 0:

            print(f"The monster hits you with {monster.strength}  strength.")
            player.take_damage(monster.strength)
            print(player)

            if player.health <= 0:
                print("You lost the fight")
                break

            print(f"You hit the monster with {player.strength} strength.")
            monster.take_damage(player.strength)
            print(monster)

        if monster.health <= 0:
            print("The monster is dead")
            regain_health = int(monster.health_init / 2)
            player.regain_health(regain_health)
            print(f"Player {player.name}, you regained health: {player.health}")

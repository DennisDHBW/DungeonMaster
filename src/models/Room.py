import time
from src.models.Player import Player
from src.models.Monster import Monster

class Room:

    COUNT_HORIZONTAL_LINE = 60

    def __init__(self, description, monster: Monster):
        self.__description = description
        self.__monster = monster

    def __str__(self):
        print(self.__description)

    @property
    def description(self):
        return self.__description

    @property
    def monster(self):
        return self.__monster

    def __fight_round(self, player: Player):

        start = time.time()
        delay = 2
        monster = self.monster

        # attack: monster
        time.sleep(delay)
        print(f"The monster hits you with {monster.strength} strength.")
        player.take_damage(monster.strength)

        # impact - attack: monster
        time.sleep(delay)
        print(player)
        if player.health <= 0:
            print("You lost the fight")
            return

        # attack: player
        time.sleep(delay)
        print(f"You hit the monster with {player.strength} strength.")
        monster.take_damage(player.strength)

        # impact - attack: player
        time.sleep(delay)
        if monster.health <= 0:
            print("+" * 60)
            print("The monster is dead")
            regain_health = int(monster.health_init / 2)
            player.regain_health(regain_health)
            print(f"Player {player.name}, you regained health: {player.health}")
        else:
            print(monster)
        print("+" * 60)

    def interact(self, player: Player):

        monster = self.monster

        print(f"Welcome to the {self.description}")
        print(f"The monster {monster.name} appears!")

        while monster.health > 0 and player.health > 0:
            action = input("Would you like to run (r) or fight (f)?")
            match action:
                case "r" | "run":
                    print("You chose RUN!")
                    player.take_damage(10)
                    print("You sprint out of the room and take 10 damage!")
                    print("+" * 60)
                    break
                case "f" | "fight":
                    print("You chose FIGHT!")
                    self.__fight_round(player)
                case _:
                    print(f"[{action}] is an invalid action.")

from src.models.Player import Player
from src.models.Monster import Monster
from src.models.Room import Room
from random import randint

def initialize_player(name: str): #unexpected
    if len(name) == 0:
        name = input("Please enter your name: ")
    strength = randint(40, 80)
    return Player(name, strength)

def initialize_monster(name):
    health = randint(40, 80)
    strength = randint(20, 40)
    return Monster(name, strength, health)

def initialize_rooms(room_config):

    rooms = []
    for config in room_config.values():
        room_name = config["desc"]
        monster_name = config["monster"]
        monster = initialize_monster(monster_name)
        rooms.append(Room(room_name, monster))
    return rooms

def print_results(player: Player):
    print("---------------------------------------------") # unexpected
    print("The game is over!")
    print(player)
    print("Thank you for playing Dungeon Master!")
    print("Good Bye!")

def create_room_config_by_userinput(nr_of_rooms):
    room_config = {}
    for room_nr in range(nr_of_rooms):
        room = input(f"Please enter a room name ({room_nr + 1} of {nr_of_rooms}): ")
        monster = input(f"Please enter a monster name ({room_nr + 1} of {nr_of_rooms}): ")
        room_config[room_nr] = {"desc": room, "monster": monster}
    return room_config

def run_game(nr_of_rooms):

    # start game
    print("Welcome to the Dungeon")
    player = initialize_player("")
    room_config = create_room_config_by_userinput(nr_of_rooms)
    rooms = initialize_rooms(room_config)

    # play game
    for room in rooms:
        room.interact(player)
        if player.health <= 0:
            print("Sorry - you died!")
            break
    print_results(player)

if __name__ == '__main__':
    run_game(5)
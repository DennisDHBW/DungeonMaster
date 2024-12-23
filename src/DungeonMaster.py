from src.models.Player import Player
from src.models.Monster import Monster
from src.models.Room import Room
from random import randint

def initialize_player():
    name = input("Please enter your name: ")
    strength = randint(40, 80)
    return Player(name, strength)

def initialize_monster(name):
    health = randint(40, 80)
    strength = randint(20, 40)
    return Monster(name, strength, health)

def initialize_rooms(room_config):

    rooms_array = []
    count_rooms = 0
    print("+"*60)
    for config in room_config.values():
        count_rooms += 1
        room_name = config["desc"]
        monster_name = config["monster"]
        print(f"[{count_rooms}] | room: {room_name} | monster: {monster_name}")
        monster = initialize_monster(monster_name)
        rooms_array.append(Room(room_name, monster))
    print("+"*60)
    return rooms_array

def print_results(player: Player):
    print("The game is over!")
    print(player)
    print("Thank you for playing Dungeon Master!\nGood Bye!")

def create_room_config_by_userinput(nr_of_rooms):
    room_config = {}
    for room_num in range(nr_of_rooms):
        room = input(f"Please enter a room name ({room_num + 1} of {nr_of_rooms}): ")
        monster = input(f"Please enter a monster name ({room_num + 1} of {nr_of_rooms}): ")
        room_config[room_num] = {"desc": room, "monster": monster}
    return room_config

def run_game(nr_of_rooms):

    # start game
    print("Welcome to the Dungeon")
    player = initialize_player()
    #room_config = create_room_config_by_userinput(nr_of_rooms)
    room_config = {
        0: {"desc": "cave", "monster": "troll"},
        1: {"desc": "home of philipp", "monster": "philipp"},
        2: {"desc": "home of dennis", "monster": "dennis"},
        3: {"desc": "home of test", "monster": "test"},
        4: {"desc": "home of test2", "monster": "test2"}
    }
    rooms = initialize_rooms(room_config)

    # play game
    for room in rooms:
        room.interact(player)
        if player.health <= 0:
            print("Sorry - you died!")
            print_results(player)
    print_results(player)

if __name__ == '__main__':
    run_game(2)
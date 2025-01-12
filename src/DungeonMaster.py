from src.models.Player import Player
from src.models.Monster import Monster
from src.models.Room import Room
import random

# funktion zur initialisierung des spielers (name + zufaellige staerke zwischen 40 und 80 + rueckgabe des spielerobjekts)
# name kann dem konstruktur uebergeben werden. falls ein leerer string uebergeben wird, kann der spieler seinen namen
# ueber die konsole eingeben.
def initialize_player(name: str): #unexpected
    if len(name) == 0:
        name = input("Please enter your name: ")
    strength = random.randint(40, 80)
    return Player(name, strength)

# funktion zur initialisierung des monsters (name + zufaellige starke zwischen 20 und 40
# + zufaelliges leben zwischen 40 und 80 + rueckgabe eines objekts vom typ monster)
def initialize_monster(name: str):
    strength = random.randint(20, 40)
    health = random.randint(40, 80)
    return Monster(name, strength, health)

# funktion zur initialisierung der raeume analog der room_config + rueckgabe eines arrays, welches objekte vom
# typ room enthaelt
def initialize_rooms(room_config):
    rooms = []
    for config in room_config.values():
        room_name = config["desc"]
        monster_name = config["monster"]
        monster = initialize_monster(monster_name)
        rooms.append(Room(room_name, monster))
    return rooms

# funktion zum ausgeben/printen der ergebnisse inkl. spieler abschluss stats
def print_results(player: Player):
    print("---------------------------------------------") # unexpected
    print("The game is over!")
    print(player)
    print("Thank you for playing Dungeon Master!")
    print("Good Bye!")

# funktion zur erstellung der room_config analog user eingaben
def create_room_config_by_userinput(nr_of_rooms):
    room_config = {}
    for room_nr in range(nr_of_rooms):
        room = input(f"Please enter a room name ({room_nr + 1} of {nr_of_rooms}): ")
        monster = input(f"Please enter a monster name ({room_nr + 1} of {nr_of_rooms}): ")
        room_config[room_nr] = {"desc": room, "monster": monster}
    return room_config

# funktion um das spiel zu starten (unter eingabe der raum anzahl)
def run_game(nr_of_rooms):

    # spielstart
    print("Welcome to the Dungeon")
    player = initialize_player("")
    room_config = create_room_config_by_userinput(nr_of_rooms)
    rooms = initialize_rooms(room_config)

    # spielen
    for room in rooms:
        room.interact(player)
        if player.health <= 0:
            print("Sorry - you died!")
            break
    print_results(player)

if __name__ == '__main__':
    run_game(5)
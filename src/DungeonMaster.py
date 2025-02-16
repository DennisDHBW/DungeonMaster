from src.models.Player import Player
from src.models.Monster import Monster
from src.models.Room import Room
import random

# funktion zur initialisierung des spielers (name + zufaellige staerke von 40 bis 80 + rueckgabe des spielerobjekts)
# name kann dem konstruktur uebergeben werden. falls ein leerer string uebergeben wird, kann der spieler seinen namen
# ueber die konsole eingeben.
def initialize_player(name: str):
    if len(name) == 0: # falls kein name uebergeben, ...
        name = input("Please enter your name: ") # ... dann kann der user ueber die konsole den namen bestimmen
    strength = random.randint(40, 80) # zufaellige staerke von 40 bis 80 (40, 41, ..., 80)
    return Player(name, strength) # gibt eine objektinstanz der klasse player zurueck

# funktion zur initialisierung des monsters (name + zufaellige starke zwischen 20 und 40
# + zufaelliges leben zwischen 40 und 80 + rueckgabe eines objekts vom typ monster)
def initialize_monster(name: str):
    strength = random.randint(20, 40) # zufaellige staerke von 20 bis 40 (20, 21, ..., 40)
    health = random.randint(40, 80) # zufaelliges leben von 40 bis 80 (40, 41, ..., 80)
    return Monster(name, strength, health) # gibt eine objektinstanz der klasse monster zurueck

# funktion zur initialisierung der raeume analog der room_config + rueckgabe einer liste, welche objekte vom
# typ room enthaelt
def initialize_rooms(room_config):
    rooms = [] # definierung einer liste
    for config in room_config.values(): # loop durch den array "room_config", welcher aus dictionaries besteht
        room_name = config["desc"] # name des raums auslesen in dem key "desc" des dicts "config" verwendet wird
        monster_name = config["monster"] # name des monsters auslesen in dem key "monster" des dicts verwendet wird
        monster = initialize_monster(monster_name) # initialisierung einer objekt instanz vom typ monster durch die entsprechende funktion
        rooms.append(Room(room_name, monster)) # liste "rooms" um eine objektinstanz der klasse room erweitert
    return rooms # liste mit objekten vom typ room wird zurueckgegeben

# funktion zum drucken bzw. printen der ergebnisse inkl. spieler abschluss stats in der konsole
def print_results(player: Player):
    print("---------------------------------------------")
    print("The game is over!")
    print(player) # zugriff auf __str__ funktion der objektinstanz der klasse player
    print("Thank you for playing Dungeon Master!")
    print("Good Bye!")

# funktion zur erstellung der room_config analog user eingaben
def create_room_config_by_userinput(nr_of_rooms):
    room_config = {} # definierung eines dictionaries
    for room_nr in range(nr_of_rooms): # loop basierend auf wert der variable nr_of_rooms
        room = input(f"Please enter a room name ({room_nr + 1} of {nr_of_rooms}): ") # user input - raum name der jeweiligen raumnummer
        monster = input(f"Please enter a monster name ({room_nr + 1} of {nr_of_rooms}): ") # user input - monster name der jeweiligen raumnummer
        room_config[room_nr] = {"desc": room, "monster": monster} # befuellen des dictionary "room_config" mit dem key "room_nr"
    return room_config # rueckgabe des dictionary "room_config" nach den erstellen x raeumen (x = nr_of_rooms)

# funktion um das spiel zu starten (unter eingabe der raum anzahl)
def run_game(nr_of_rooms):

    # spielstart
    print("Welcome to the Dungeon")
    player = initialize_player("") # objektinstanz der klasse player initialisieren und in der variable player speichern (durch die entsprechende funktion)
    room_config = create_room_config_by_userinput(nr_of_rooms) # variable room_config mit der entsprechenden funktion initialisieren
    rooms = initialize_rooms(room_config) # variable rooms mit der enstprechenden funktion initialisieren

    # spielen
    for room in rooms: # loop durch alle raeume
        if player.health > 0: # wenn player nicht tot bzw. leben groesser 0 dann ...
            room.interact(player) # ... rufe objektfunktion "interact" der objektinstanz "room" vom typ room auf
        if player.health <= 0: # wenn player tot bzw. leben kleiner gleich 0 dann ...
            print("Sorry - you died!") # benachrichte den spieler in der konsole ...
            break # ... und brich den schleifendurchlauf ab
    print_results(player) # nach dem spiel, wird die funktion "print_results" mit dem spieler objekt aufgerufen

if __name__ == '__main__':
    run_game(5)
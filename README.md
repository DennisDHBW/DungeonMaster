# Prüfungsleistung - Dungeon Escape

In dieser Aufgabe entwickeln Sie eine Python-Anwendung, die ein vereinfachtes Dungeon-Abenteuer darstellt. Dabei
steuert ein Spieler durch eine Reihe von Räumen, in denen Monster warten. Der Spieler kämpft gegen die Monster, um
aus dem Dungeon zu entkommen.

Das Projekt besteht aus vier Dateien: DungeonMaster, Monster, Player, und Room. Zusätzlich gibt es einige
unterstützende Funktionen, die das Spiel initialisieren und steuern.

Arbeiten Sie sich nacheinander durch die einzelnen anzulegenden Dateien wie im Folgenden beschrieben.

## Klasse `Player` in Datei `Player.py`

### Instanzvariablen

Die Klasse `Player` enthält die folgenden privaten Instanzvariablen:

- `name`: Name des Spielers wird dem Konstruktor übergeben
- `health`: Gesundheitszustand des Spielers (soll standardmäßig auf den Wert 100 gesetzt werden)
- `strength`: Stärke des Spielers wird dem Konstruktor übergeben (zufällige Zahl zwischen 40 (inkl.) und 80 (inkl.))

### Methoden

Folgende Methoden sind zu implementieren:

- `__str__` soll folgenden String zurückgeben: "Player <name> has <strength> strength and <health> health."
- `take_damage(damage)` soll eine Zahl `damage` als Parameter erhalten und diesen vom aktuellen `health`
  Wert abziehen (Minimalwert: 0)
- `regain_health(health_regain)` soll eine Zahl `health_regain` als Parameter erhalten und diese auf die aktuelle
  `health` addieren (Maximalwert ist der Standardwert 100)

## Klasse `Monster` in Datei `Monster.py`

### Instanzvariablen

Die Klasse `Monster` enthält die folgenden privaten Instanzvariablen:

- `name`: Name des Monsters wird dem Konstruktor übergeben
- `strength`: Stärke des Monsters wird dem Konstruktor übergeben (zufälliger Wert zwischen 20 (inkl.) und 40 (inkl.))
- `health`: Gesundheitszustand des Monsters wird dem Konstruktor übergeben (zufälliger Wert zwischen 40 (inkl.) und 80 (
  inkl.))

### Methoden

- `__str__` soll folgenden String zurückgeben: "Monster <name> has <strength> strength and <health> health."
- `take_damage(damage)` soll dem Monster den übergebenen Schaden vom Gesundheitszustand abziehen

## Klasse `Room` in Datei `Room.py`

### Instanzvariablen

Die Klasse `Room` enthält die folgenden privaten Instanzvariablen:

- `description`: Beschreibung des Raums wird dem Konstruktor übergeben
- `monster`: Monster, das sich im Raum befindet, wird dem Konstruktor übergeben

### Methoden

- `__str__` soll die Raumbeschreibung (`description`) zurückgeben
- `fight_round(player)`: soll eine Runde eines Kampfes zwischen Spieler und Monster austragen. Dabei gilt folgender
  Ablauf:
    1. Monster schlägt zu:
        1. Ausgabe: "The monster hits you with <monster-strength> strength."
        2. Spieler erhält Schaden (`damage`) in Höhe der Stärke (`strength`) des Monsters.
        3. Ausgabe des Spieler-Objekts
    2. Spieler greift an:
        1. Ausgabe: "You hit the monster with <player-strength> strength."
        2. Monster erhält Schaden (`damage`) in Höhe der Stärke (`strength`) des Spielers.
        3. Ausgabe des Monster-Objekts
    3. Falls das Monster geschlagen wurde (Gesundheit = 0)
        1. Ausgabe: "The monster is dead"
       2. Spieler erhält Gesundheitspunkte in Höhe der Hälfte des vom Monsters erlittenen Schadens (z.B.: in einem
           Kampf erleidet ein Monster 60 Schadenspunkte. Sobald der Spieler das Monster getötet hat, erhält der Spieler
          60/2 = 30 Punkte auf seinen Gesundheitszustand gutgeschrieben)
        3. Ausgabe: Player <player-name>, you regained health: <player-health>"
    4. Falls der Spieler geschlagen wurde (Gesundheit = 0)
        1. Ausgabe: "You lost the fight"
- `interact(player)`: In dieser Methode interagiert der Spieler mit dem Raum. Dabei gilt folgender Ablauf:
    1. Ausgabe: "Welcome to the <raum-description>" und "The monster <monster-name> appears!")
    2. Ab sofort wird das Folgende in Runden wiederholt, bis entweder der Spieler oder das Monster keine Gesundheit mehr
       haben (Gesundheit = 0)
        1. Abfrage, ob der Spieler weglaufen oder kämpfen möchte: "Would you like to run (r) or fight (f)?"
        2. Bei Wahl `r` (weglaufen): Ausgabe: "You chose RUN!", Spieler erhält 10 Schadenspunkte, Ausgabe: "You sprint
           out of the room and take 10 damage!" und Ausgabe Spieler-Objekt
        3. Wenn der Spieler den Kampf wählt: Ausgabe: "You chose FIGHT!" und Ablauf einer Kampf-Runde (siehe Methode
           `fight_round()`)

## Datei `DungeonMaster.py`

Die Datei `DungeonMaster.py` enthält lediglich die Spiellogik und keine eigene Klasse.

Die folgenden Methoden sind zu implementieren:

- `__main__`: setzt die Anzahl an Räumen des Dungeons auf 5 und startet das Spiel mit dem Funktionsaufruf `run_game()`
- `initialize_player()`: Diese Methode initialisiert den Spieler, indem Sie den Namen des Spielers abfragt und die
  Stärke des Spielers (`strength`) auf eine zufällige Zahl zwischen 40 und 80 setzt.
- `initialize_rooms(rooms)`: Diese Methode erhält in einem Dictionary die Informationen zu allen Räumen.
    - Das übergebene Dictionary soll so aufgebaut sein:
       ```python
       rooms = { 0: {"desc": "Dark Cave", "monster": "Goblin"},
				 1: {"desc": "Bright Hall", "monster": "Orc"}
				}
      ...
    - Die Methode erhält das Dictionary und gibt eine Liste mit allen Räumen (inkl. Monster) zurück
    - Die Gesundheit der zu erstellenden Monster soll jeweils ein zufälliger Wert zwischen 40 und 80 sein.
    - Die Stärke der zu erstellenden Monster soll jeweils ein zufälliger Wert zwischen 20 und 40 sein.
- `print_results(player)`: Diese Methode soll das Ergebnis des gesamten Spiels ausgeben. Zuerst die Zeichenkette
  "The game is over!"), dann das Spieler-Objekt, dann "Thank you for playing Dungeon Master!" und schließlich "Good
  Bye!".
- `run_game(nr_of_rooms)`: Diese Methode startet das Spiel nach folgendem Ablauf:
    1. Ausgabe: "Welcome to the Dungeon" und Initialisierung des Spielers
    2. Abfragen der Raumkonfiguration vom Nutzer (für jeden zu erstellenden Raum soll die Raumbeschreibung als auch
       der Name des Monsters vom Nutzer abgefragt werden)
    3. Mit Hilfe der Funktion `initialize_rooms(room_config)` und der eingegebenen Informationen vom Nutzer sollen die
       Räume nun erstellt werden
    4. Anschließend betritt der Spieler der Reihe nach alle Räume im Dungeon und interagiert mit diesen.
    5. Sobald der Spieler 0 Gesundheitspunkte hat, soll "Sorry - you died!" ausgegeben und die Methode `print_results
       (player)` aufgerufen werden.

## Hilfestellung und Hinweise

- Die vorgegebene Struktur der Dateien, Klassen und Methoden ist einzuhalten.
- Weitere Klassen/Methoden etc. können bei Bedarf ergänzt werden.

- Implementieren Sie zuerst die Klassen `Player` und `Monster` und testen Sie diese mit den jeweiligen
  Unit-Tests (`Test_Player.py` und `Test_Monster.py`)
- Implementieren Sie dann die Klasse `Room` und testen Sie auch diese mit den Unit-Tests in (`test_Room.py`)
- Implementieren Sie dann eine vereinfachte Logik der Datei `DungeonMaster.py` in der Sie den Spieler, die Monster
  und Räume erstellen und den Spieler die einzelnen Räume betreten lassen.
- Schließen Sie Ihre Implementierung ab, indem Sie die Datei `DungeonMaster.py` nach den Vorgaben fertig implementieren.

## Abgabe

1. Prüfen Sie, ob alle Unit-Tests erfolgreich ausgeführt werden können
2. Kommentieren Sie Ihren Code umfassend, sodass die Eigenständigkeit Ihrer Abgabe nachvollziehbar ist
3. Verpacken Sie Ihren Code als .zip-Datei und laden Sie diese im Moodle Kursraum zur Vorlesung hoch
4. Beantworten Sie die folgenden Fragen zur Reflexion Ihrer Prüfungsleistung im Moodle Kursraum in wenigen Sätzen
   (Achtung! Die Abgabe wird nur als vollständig gewertet, wenn Sie die Fragen ebenfalls beantwortet haben!)
    1. Was war Ihre größte Herausforderung bei der Implementierung der Aufgabe?
    2. Welche Fehler/Bugs sind im Verlauf der Implementierung aufgetreten? Wie haben Sie diese gefunden und gelöst?
    3. Welche Konzepte der Objektorientierten Programmierung haben Sie im Projekt angewandt?
    4. Wie könnten Sie dieses Projekt in Zukunft erweitern, um das Spiel interessanter oder komplexer zu machen?
5. Geben Sie Ihren Code, sowie die Antworten zu den Fragen im Moodle Kursraum ab.

---

4. Beantworten Sie die folgenden Fragen zur Reflexion Ihrer Prüfungsleistung im Moodle Kursraum in wenigen Sätzen
   (Achtung! Die Abgabe wird nur als vollständig gewertet, wenn Sie die Fragen ebenfalls beantwortet haben!)
    1. Was war Ihre größte Herausforderung bei der Implementierung der Aufgabe?
        - Teilweise musste ich feststellen, dass ich etwas vom Skript abgewichen bin. Das habe ich dann nachträglich angepasst.
        - Unit-Tests wurden bisher nicht behandelt. Daher musste ich mich online einlesen wie man Unit-Tests nutzt.
        - Teilweise habe ich Funktionen hinzugefügt, die ich gerne eingebaut hätte, welche ich jedoch nachträglich wieder entfernt habe.
        - Ich habe den Satz "Diese Methode initialisiert den Spieler, indem Sie den Namen des Spielers abfragt und [...]" 
          falsch verstanden, da laut Unit Test dem Konstruktur der Methode "initialize_player" ein Name übergeben wird. Damit der Unit Test nicht fehlschlägt und ich die input Aufforderung weiterhin innerhalb der Methode "initialize_player" lassen kann, habe ich eine zusätzliche Abfrage eingebaut, welche prüft ob ein leerer String übergeben wurde. Falls ja, dann user input.
        - Verständnis der Anforderungen und exakte Umsetzung der Anforderungen

    2. Welche Fehler/Bugs sind im Verlauf der Implementierung aufgetreten? Wie haben Sie diese gefunden und gelöst?
        - Funktion "lost_health" verursachte Fehler im Unit Test --> Funktion dem Code hinzugefügt 
        - Funktion "regain_health" nicht von Anfang an mit int gecastet (double war möglich) --> wert auf int gecastet
        - Funktion "print_results" haben die Striche gefehlt, welche im Unit Test erwartet wurden --> nachträglich eingefügt
        - Funktion "initialize_player" verursachte im Unit Test einen Fehler, da ein String übergeben werden muss. Ich bevorzuge den User input, jedoch in der Funktion.

    3. Welche Konzepte der Objektorientierten Programmierung haben Sie im Projekt angewandt?
        - Erstellung von Klassen
        - Definierung von Instanzvariablen des Klassenobjekts
        - Private Instanzvariablen, welche durch getter-Methoden abgefragt werden können
        - Importierung der erstellten Klassenbibliotheken
        - Erstellung von Objektinstanzen aus Klassen, z.B. Monster und Raum
        - Magic Methods (__init__ und __str__)

    4. Wie könnten Sie dieses Projekt in Zukunft erweitern, um das Spiel interessanter oder komplexer zu machen?
        - Verzögerungen zwischen den Angriffen mit der sleep Funktion   
        - Schwierigkeitsstufen
        - Speicherfunktion (speichern und laden des Spielfortschritts)
        - Items (Tränke, Rüstung, Waffen, ...)
        - Fähigkeiten (Ausweichen, Täuschen, ...)
        - Mehr Variation durch zufällige kritische Treffer

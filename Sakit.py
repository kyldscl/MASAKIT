import time
import sys

angsakitmo = [
    ("And I hope I never lose you,", 2, 0.09),
    ("hope it never ends", 2.4, 0.10),
    ("I'd never walk Cornelia Street again", 3.0, 0.10),
    (" ", 2.5, 1), 
    ("That's the kind of heartbreak time could never mend", 3.5, 0.09),
    ("I'd never walk Cornelia Street again", 4.5, 0.10),
    (" ", 4.0, 0.8),
    ("And baby, I get mystified by how this", 4, 0.15),
    (" ", 2.0, 0.2),
    ("City screams your name", 3.0, 0.12),
    (" ", 2.0, 0.8),
    ("And baby, I'm so terrified of if you ever walk away", 5.5, 0.15),
    ("I'd never walk Cornelia Street again", 3.8, 0.10),
    (" ", 5.0, 0.8),
    ("I'd never walk Cornelia Street again", 5.0, 0.12)
]
def type_line(line, typing_speed):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()

def angsakitmopo(angsakitmo):
    for line, delay, speed in angsakitmo:
        type_line(line, speed)
    time.sleep(delay)

angsakitmopo(angsakitmo)
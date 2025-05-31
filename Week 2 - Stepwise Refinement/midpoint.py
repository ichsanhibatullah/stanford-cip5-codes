from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    mark_end_start()
    while no_beepers_present():
        move_beeper_closer()
    fencepost_beeper()
    go_to_last_beeper()

def mark_end_start():
    for i in range(2): #Mark END first then START
        while front_is_clear() and no_beepers_present():
            move()
        put_beeper()
        turn_around()
        move()

def move_beeper_closer():
    while front_is_clear() and no_beepers_present():
        move()
    pick_beeper()
    turn_around()
    move()
    put_beeper()
    move()

def fencepost_beeper():
    # Fencepost Bug(?)
    pick_beeper()

def go_to_last_beeper():
    turn_around()
    move()
    turn_around()
    if facing_west():
        turn_around()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()
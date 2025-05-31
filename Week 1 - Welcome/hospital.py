from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()

def build_hospital():
    """Build a hospital (3x2 building)
    Pre-cond: Karel facing East on ground floor
    Post-cond: Karel facing East on ground floor
    """
    build_from_ground()
    move_next_column()
    build_from_top()

def build_from_ground():
    """Build first part of building from ground
    Pre-cond: Karel facing East on ground floor
    Post-cond: Karel facing North on highest floor
    """
    turn_left()
    for i in range(2):
        move()
        put_beeper()

def move_next_column():
    """Move to next column of the building
    Pre-cond: Karel facing North on highest floor
    Post-cond: Karel facing South on highest floor
    """
    turn_right()
    move()
    turn_right()

def build_from_top():
    """Build second part of building from top
    Pre-cond: Karel facing South on highest floor
    Post-cond: Karel facing East on ground floor
    """
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
    turn_left()

def turn_right():
    """Helper function: Turn Right"""
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
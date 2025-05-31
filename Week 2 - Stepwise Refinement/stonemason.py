from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #pass
    while front_is_clear():
        create_pillar()
        move_next_column()
    create_pillar()

def create_pillar():
    turn_left()
    build()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    
def build():
    for i in range(4):
        put_beeper()
        move()
    put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

def move_next_column():
    for i in range(4):
        move()


if __name__ == '__main__':
    main()
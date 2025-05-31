from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #pass
    move()
    while beepers_present():
        pick_beeper()
        if no_beepers_present():
            put_beeper()
            turn_home()
        else:
            spread_beeper()
            turn_home()
            move()          # Back to pile of beepers

def spread_beeper():
    while beepers_present():
        move()
    put_beeper()      

def turn_home():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
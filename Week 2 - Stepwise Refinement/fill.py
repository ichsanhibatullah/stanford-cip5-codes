from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #pass
    while left_is_clear():
        fill_beepers()
        move_next_row()
    # Fence Post Bug
    fill_beepers()

def fill_beepers():
    while front_is_clear():
        put_beeper()
        move()
    # Fence Post Bug
    put_beeper()

def move_next_row():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
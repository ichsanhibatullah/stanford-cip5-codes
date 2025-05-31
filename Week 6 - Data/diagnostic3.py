from karel.stanfordkarel import *

def main():
    # move()
    # TODO: your code here
    while front_is_clear():
        put_beeper()
        move()
        build_two_beepers()
        back_first_row()

        for i in range(2):
            safe_move()

def build_two_beepers():
    turn_left()
    put_beeper()
    move()
    put_beeper()

def back_first_row():
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def safe_move():
    if front_is_clear():
        move()

def turn_around():
    for i in range(2):
        turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
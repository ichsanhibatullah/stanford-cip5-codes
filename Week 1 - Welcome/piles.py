from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    # your code here
    while front_is_clear():
        while beepers_present():
            pick_beeper()
        move()
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 25 beepers, and end facing East to 
the right of the 25 beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(20):
        put_beeper()
    move()
    for i in range(25):
        put_beeper()
    move()

if __name__ == '__main__':
    main()
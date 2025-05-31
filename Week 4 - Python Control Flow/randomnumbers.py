import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    # pass
    for i in range(10):
        val = random.randint(MIN_VALUE, MAX_VALUE)
        print(val)

if __name__ == '__main__':
    main()
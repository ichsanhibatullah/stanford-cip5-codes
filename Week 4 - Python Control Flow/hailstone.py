"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    # your code here
    # pass
    input_number = int(input("Enter a number: "))
    while input_number != 1:
        if input_number % 2 == 0:
            print(f"{input_number} is even, so I take half: {int(input_number / 2)}")
            input_number = int(input_number / 2)
        else: # the remainder is one
            print(f"{input_number} is odd, so I make 3n + 1: {3 * input_number + 1}")
            input_number = 3 * input_number + 1

if __name__ == "__main__":
    main()
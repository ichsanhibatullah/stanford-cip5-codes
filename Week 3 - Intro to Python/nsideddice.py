import random

def main():
    # print("Delete this line and write your code here! :)")
    side_input = int(input("How many sides does your dice have? "))
    roll = random.randint(1, side_input)
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()
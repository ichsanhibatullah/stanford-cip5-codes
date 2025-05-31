import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Define initial score
    score = 0
    
    # TODO: Write your code here!!! :)
    for i in range(NUM_ROUNDS):
        comp_num = random.randint(1, 100)
        user_num = random.randint(1, 100)

        print('Round '+ str(i + 1))
        # print(f"The computer's number is {comp_num}")
        print(f"Your number is {user_num}")

        highlow = input("Do you think your number is higher or lower than the computer's?: ")
        while highlow.lower() != 'higher' and highlow.lower() != 'lower':
            highlow = input("Please enter either higher or lower: ")

        if (highlow.lower() == 'higher' and user_num > comp_num) or (highlow.lower() == 'lower' and user_num < comp_num):
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        
        print(f"Your score is now {score}")
        print("")
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= score // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
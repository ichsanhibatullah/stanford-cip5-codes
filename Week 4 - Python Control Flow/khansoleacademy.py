import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    ## 1st
    first_num = random.randint(10, 99)
    second_num = random.randint(10, 99)
    ground_truth = first_num + second_num
    print(f'What is {first_num} + {second_num}?')
    answer = int(input('Your answer: '))
    if answer == ground_truth:
        print('Correct!')
    else:
        print('Incorrect.')
        print(f'The expected answer is {ground_truth}')

    ## 2nd
    # streak = 0
    # while streak < 3:
    #     first_num = random.randint(10, 99)
    #     second_num = random.randint(10, 99)
    #     ground_truth = first_num + second_num
    #     print(f'What is {first_num} + {second_num}?')
    #     answer = int(input('Your answer: '))
    #     if answer == ground_truth:
    #         print('Correct!')
    #         streak += 1
    #         print(f"You've gotten {streak} correct in a row.")
    #         print('')
   
    #     else:
    #         print('Incorrect.')
    #         print(f'The expected answer is {ground_truth}')
    #         print('')
    #         streak = 0
    # if streak == 3:
    #     print('Congratulations! You mastered addition.')
    
if __name__ == '__main__':
    main()
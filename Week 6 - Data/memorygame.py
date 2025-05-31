import random

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    # pass
    truth = []; display = []
    for i in range(NUM_PAIRS):
        for j in range(2):
            truth.append(i)
            display.append('*')

    random.shuffle(truth)

    while '*' in display:
        clear_terminal()

        print(display)
        
        get_index_one = get_valid_index(truth, display)
        get_index_two = get_valid_index(truth, display)
        while get_index_one == get_index_two:
            print("Can't be the same index.")
            get_index_two = get_valid_index(truth, display)

        if truth[get_index_one] == truth[get_index_two]:
            print('Match!')
            display[get_index_one] = truth[get_index_one]
            display[get_index_two] = truth[get_index_two]
        else:
            print(f"Value at index {get_index_one} is {truth[get_index_one]}")
            print(f"Value at index {get_index_two} is {truth[get_index_two]}")
            print("No match. Try again. Press Enter to continue...")
            input("Press Enter to continue...")

    clear_terminal()
    if '*' not in display:
        print(display)
        print('Congratulations! You won!')


def get_valid_index(truth_list, display_list):
    idx = int(input("Enter an index: "))
    if idx < 0 or idx >= len(truth_list):
        idx = int(input("Enter a valid index: "))
    if display_list[idx] != '*':
        idx = int(input("Enter an unguessed index: "))
    return idx

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
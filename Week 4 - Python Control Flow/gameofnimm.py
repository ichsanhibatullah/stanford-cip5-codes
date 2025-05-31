def main():
    """
    You should write your code here. 
    """
    #print("The Ancient Game of Nimm")  # Delete this line and write your code here! :)
    stones_count = 20

    while stones_count > 0:
        print(f'There are {stones_count} stones left.')
        stone_remove_p1 = int(input('Player 1 would you like to remove 1 or 2 stones? '))
        while stone_remove_p1 != 1 and stone_remove_p1 != 2:
            stone_remove_p1 = int(input("Please enter 1 or 2: "))
        stones_count -= stone_remove_p1
        print('')

        if stones_count > 0:
            print(f'There are {stones_count} stones left.')
            stone_remove_p2 = int(input('Player 2 would you like to remove 1 or 2 stones? '))
            while stone_remove_p2 != 1 and stone_remove_p2 != 2:
                stone_remove_p2 = int(input("Please enter 1 or 2: "))
            stones_count -= stone_remove_p2
            print('')
            if stones_count <= 0:
                print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    #print('Game over')

if __name__ == '__main__':
    main()
def main():
    # TODO write your solution here
    # pass
    greater_than = True
    sequence = 1

    print("Enter a sequence of non-decreasing numbers.")
    initial_num = float(input("Enter num: "))
    
    while greater_than:
        compared_num = float(input("Enter num: "))
        if compared_num >= initial_num:
            initial_num = compared_num
            sequence += 1
        else:
            print("Thanks for playing!")
            print(f"Sequence length: {sequence}")
            greater_than = False
        
if __name__ == "__main__":
    main()
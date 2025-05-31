# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # pass
    # TODO: your code here
    for i in range(MAX_NUMBER):
        current_num = i + 1
        if current_num % 2 == 0:
            print(f"{current_num} is even")
        else:
            print(f"{current_num} is odd")

if __name__ == "__main__":
    main()
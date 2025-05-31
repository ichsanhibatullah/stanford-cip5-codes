def main():
    # TODO write your solution here
    # pass
    input_height = float(input("Enter your height in meters: "))

    if input_height > 1.6 and input_height < 1.9:
        print("Correct height to be an astronaut")
    elif input_height <= 1.6:
        print("Below minimum astronaut height")
    elif input_height >= 1.9:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
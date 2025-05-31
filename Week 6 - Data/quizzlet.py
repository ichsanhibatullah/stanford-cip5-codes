def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    # pass  # Delete this line and write your code here! :)
    count_true = 0
    for key, value in translations.items():
        answer = input(f"What is the Spanish translation for {key}? ")
        if answer == value:
            print("That is correct!")
            print("")
            count_true += 1
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.")
            print("")
    print(f"You got {count_true}/{len(translations)} words correct, come study again soon!")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
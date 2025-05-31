from ai import call_gpt

def main():
    # TODO: your code here
    #pass
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")

    response = call_gpt(f"Create a Haiku using as {name} name, and {topic} as the topic.")
    print(response)

if __name__ == "__main__":
    main()
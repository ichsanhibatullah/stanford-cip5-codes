"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    # pass
    weight = float(input("Enter a weight on Earth: "))
    equivalent_weight = weight * 0.378
    rounded_equivalent_weight = round(equivalent_weight, 2)
    print(f"The equivalent weight on Mars: {rounded_equivalent_weight}")

if __name__ == "__main__":
    main()
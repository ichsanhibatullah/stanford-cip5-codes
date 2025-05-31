"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
# MERCURY = 0.376
# VENUS = 0.889
# MARS = 0.378
# JUPITER = 0.2360
# SATURN = 1.081
# URANUS = 0.815
# NEPTUNE = 1.140

planets = {
    'MERCURY': 0.376,
    'VENUS': 0.889,
    'MARS': 0.378,
    'JUPITER': 2.360,
    'SATURN': 1.081,
    'URANUS': 0.815,
    'NEPTUNE': 1.140
    }

def main():
    # Fill this function out!
    # pass
    weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet.upper() in planets:
        eq_weight = round(weight * planets[planet.upper()], 4)
    else:
        print("Your planet is not registered yet. Please input the correct planet.")

    print(f"The equivalent weight on {planet}: {eq_weight}")


if __name__ == "__main__":
    main()
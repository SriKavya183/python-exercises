Exercise 36: Dog Years


human_years = float(input("Enter age in human years: "))

if human_years < 0:
    print("Error: Age cannot be negative.")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print("Dog years:", dog_years)
else:
    dog_years = (2 * 10.5) + ((human_years - 2) * 4)
    print("Dog years:", dog_years)

--------------------------------------------------------

Exercise 37: Vowel or Consonant

letter = input("Enter a letter: ").lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("It is a vowel.")
elif letter == 'y':
    print("Sometimes 'y' is a vowel, sometimes a consonant.")
else:
    print("It is a consonant.")

----------------------------------------------------------

Exercise 38: Name That Shape

sides = int(input("Enter number of sides: "))

if sides == 3:
    shape = "Triangle"
elif sides == 4:
    shape = "Quadrilateral"
elif sides == 5:
    shape = "Pentagon"
elif sides == 6:
    shape = "Hexagon"
elif sides == 7:
    shape = "Heptagon"
elif sides == 8:
    shape = "Octagon"
elif sides == 9:
    shape = "Nonagon"
elif sides == 10:
    shape = "Decagon"
else:
    shape = None

if shape:
    print(f"The shape with {sides} sides is a {shape}.")
else:
    print(f"Error: {sides} is not supported (3–10 only).")

------------------------------------------------------------------------------
Exercise 39: Month Name to Days

month = input("Enter month name: ").lower()

if month in ["april", "june", "september", "november"]:
    print(f"{month.title()} has 30 days.")
elif month == "february":
    print(f"{month.title()} has 28 or 29 days.")
elif month in ["january", "march", "may", "july", "august", "october", "december"]:
    print(f"{month.title()} has 31 days.")
else:
    print("Invalid month name.")

-----------------------------------------------------

Exercise 40: Sound Levels

db = int(input("Enter sound level (dB): "))

if db == 130:
    print("Jackhammer")
elif db == 106:
    print("Gas Lawnmower")
elif db == 70:
    print("Alarm Clock")
elif db == 40:
    print("Quiet Room")
elif db < 40:
    print(f"{db} dB is quieter than a Quiet Room.")
elif db > 130:
    print(f"{db} dB is louder than a Jackhammer.")
elif 40 < db < 70:
    print(f"{db} dB is between Quiet Room and Alarm Clock.")
elif 70 < db < 106:
    print(f"{db} dB is between Alarm Clock and Gas Lawnmower.")
elif 106 < db < 130:
    print(f"{db} dB is between Gas Lawnmower and Jackhammer.")

-----------------------------------------------------------------------

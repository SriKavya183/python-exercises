Exercise 46: Chess Square Color

pos = input("Enter position: ")

col = pos[0]
row = int(pos[1])

if col in "aceg":
    base = "black"
else:
    base = "white"

if row % 2 == 0:
    color = "white" if base == "black" else "black"
else:
    color = base

print(f"The square {pos} is {color}.")

------------------------------------------------------
Exercise 47: Season

month = input("Enter month: ").lower()
day = int(input("Enter day: "))

if (month == "march" and day >= 20) or month in ["april", "may"] or (month == "june" and day <= 20):
    season = "Spring"
elif (month == "june" and day >= 21) or month in ["july", "august"] or (month == "september" and day <= 21):
    season = "Summer"
elif (month == "september" and day >= 22) or month in ["october", "november"] or (month == "december" and day <= 20):
    season = "Fall"
else:
    season = "Winter"

print(f"The season is {season}.")

--------------------------------------------------------
Exercise 48: Zodiac Sign

month = input("Enter month: ").lower()
day = int(input("Enter day: "))

if (month == "march" and day >= 21) or (month == "april" and day <= 19):
    sign = "Aries"
elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
    sign = "Taurus"
elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
    sign = "Gemini"
else:
    sign = "Capricorn"

print(f"Your zodiac sign is {sign}.")

-------------------------------------------------------------------------------
Exercise 49: Chinese Zodiac

year = int(input("Enter year: "))

animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster",
           "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]

index = (year - 2000) % 12

print(f"The year {year} is the year of the {animals[index]}.")

-------------------------------------------------------------------------

Exercise 50: Richter Scale

mag = float(input("Enter magnitude: "))

if mag < 2.0:
    desc = "Micro"
elif mag < 3.0:
    desc = "Very Minor"
elif mag < 4.0:
    desc = "Minor"
elif mag < 5.0:
    desc = "Light"
elif mag < 6.0:
    desc = "Moderate"
elif mag < 7.0:
    desc = "Strong"
elif mag < 8.0:
    desc = "Major"
elif mag < 10.0:
    desc = "Great"
else:
    desc = "Meteoric"

print(f"A magnitude {mag} earthquake is {desc}.")





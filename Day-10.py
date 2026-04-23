Exercise 41: Classifying Triangles

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

----------------------------------------------------
Exercise 42: Note to Frequency

note = input("Enter note: ").upper()

note_base = note[0]
octave = int(note[1])

freqs = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

base_freq = freqs[note_base]
frequency = base_freq / (2 ** (4 - octave))

print(f"The frequency of {note} is {frequency:.2f} Hz.")


---------------------------------------------------------
Exercise 43: Frequency to Note

freq = float(input("Enter frequency: "))

notes = {
    261.63: "C4",
    293.66: "D4",
    329.63: "E4",
    349.23: "F4",
    392.00: "G4",
    440.00: "A4",
    493.88: "B4"
}

found = False

for f in notes:
    if abs(freq - f) <= 1:
        print(f"The note is {notes[f]}")
        found = True
        break

if not found:
    print("No matching note found.")
-----------------------------------------------------

Exercise 44: Faces on Money

amount = int(input("Enter banknote amount: "))

people = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"
}

if amount in people:
    print(f"${amount} features {people[amount]}.")
else:
    print("Invalid denomination.")
-------------------------------------------------------------
Exercise 45: Date to Holiday
month = input("Enter month: ").lower()
day = int(input("Enter day: "))

if month == "january" and day == 1:
    print("New Year's Day")
elif month == "july" and day == 1:
    print("Canada Day")
elif month == "december" and day == 25:
    print("Christmas Day")
else:
    print("Not a fixed-date holiday.")



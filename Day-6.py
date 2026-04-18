Exercise 21: Area of a Triangle (base & height)
b = float(input("Enter base: "))
h = float(input("Enter height: "))

area = (b * h) / 2

print(f"Area of triangle: {area:.2f}")

---------------------------------------------
Exercise 22: Area of Triangle (3 sides - Heron’s Formula)

import math

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area of triangle: {area:.2f}")

--------------------------------------------------------------

Exercise 23: Area of Regular Polygon

import math

s = float(input("Enter side length: "))
n = int(input("Enter number of sides: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"Area of polygon: {area:.2f}")

-------------------------------------------------------
Exercise 24: Units of Time → Convert to Seconds

days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = (
days * 86400 +
hours * 3600 +
minutes * 60 +
seconds
)

print(f"Total seconds: {total_seconds}")

--------------------------------------------------

Exercise 25: Seconds → D:HH:MM:SS


seconds = int(input("Enter total seconds: "))

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")


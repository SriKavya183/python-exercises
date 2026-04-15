Exercise-11-Fuel Efficiency (MPG → L/100 km)
mpg = float(input("Enter fuel efficiency in MPG: "))
l_per_100km = 235.215 / mpg
print(f"Fuel efficiency: {l_per_100km:.2f} L/100 km")

------------------------------------------------------------------

Exercise-12- Distance Between Two Points on Earth
import math
t1 = float(input("Enter latitude of point 1: "))
g1 = float(input("Enter longitude of point 1: "))
t2 = float(input("Enter latitude of point 2: "))
g2 = float(input("Enter longitude of point 2: "))
t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)
distance = 6371.01 * math.acos(
    math.sin(t1) * math.sin(t2) +
    math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
)

print(f"Distance between the two points: {distance:.2f} km")

-----------------------------------------------------------------------------

Exercise-13 - Making Change

cents = int(input("Enter amount in cents: "))
toonies = cents // 200
cents %= 200

loonies = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print(f"Toonies: {toonies}")
print(f"Loonies: {loonies}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

---------------------------------------------------------------
 Exersice-14 - Height Units

feet = int(input("Enter height (feet): "))
inches = int(input("Enter remaining inches: "))

total_inches = (feet * 12) + inches

cm = total_inches * 2.54

print(f"Height in centimeters: {cm:.2f} cm")

--------------------------------------------------------------------------
Exercise-15- Distance Units

# Read distance in feet
feet = float(input("Enter distance in feet: "))

# Conversions
inches = feet * 12
yards = feet / 3
miles = feet / 5280

# Display results
print(f"Inches: {inches:.2f}")
print(f"Yards: {yards:.2f}")
print(f"Miles: {miles:.6f}")




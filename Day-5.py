Exercise 16: Area and Volume

import math

r = float(input("Enter radius: "))

area = math.pi * r**2
volume = (4/3) * math.pi * r**3

print(f"Area of circle: {area:.2f}")
print(f"Volume of sphere: {volume:.2f}")

------------------------------------------------------------
Exercise 17: Heat Capacity

mass = float(input("Enter mass (grams): "))
delta_t = float(input("Enter temperature change (°C): "))

C = 4.186

q = mass * C * delta_t

kwh = q / 3_600_000

cost = kwh * 8.9  
print(f"Energy required: {q:.2f} Joules")
print(f"Energy in kWh: {kwh:.6f}")
print(f"Cost: {cost:.4f} cents")

-----------------------------------------------------------

Exercise 18: Volume of a Cylinder

import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

volume = math.pi * r**2 * h

print(f"Volume of cylinder: {volume:.1f}")

--------------------------------------------------------
Exercise 19: Free Fall

import math

d = float(input("Enter height (meters): "))

a = 9.8

vf = math.sqrt(2 * a * d)

print(f"Final velocity: {vf:.2f} m/s")

--------------------------------------------------------------
Exercise 20: Ideal Gas Law

P = float(input("Enter pressure : "))
V = float(input("Enter volume : "))
T_c = float(input("Enter temperature : "))

R = 8.314

T_k = T_c + 273.15

n = (P * V) / (R * T_k)

print(f"Number of moles: {n:.2f}")





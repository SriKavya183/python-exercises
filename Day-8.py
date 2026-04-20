Exercise 31: Pressure Conversion

kpa = float(input("Enter pressure in kilopascals: "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa / 101.325

print(f"PSI: {psi:.2f}")
print(f"mmHg: {mmhg:.2f}")
print(f"Atmospheres: {atm:.4f}")

-------------------------------------------------

Exercise 32: Sum of Digits

num = int(input("Enter a 4-digit number: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

total = d1 + d2 + d3 + d4

print(f"{d1}+{d2}+{d3}+{d4} = {total}")

---------------------------------------------------
Exercise 33: Sort 3 Integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

small = min(a, b, c)
large = max(a, b, c)
middle = a + b + c - small - large

print(f"Sorted order: {small}, {middle}, {large}")

--------------------------------------------------------
Exercise 34: Day Old Bread

loaves = int(input())

price = 3.49
discount_rate = 0.60

regular = loaves * price
discount = regular * discount_rate
total = regular - discount

print(f"Regular price: {regular:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Total price: {total:.2f}")

-------------------------------------------
Exercise 35: Even or Odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

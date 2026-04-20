Exercise 26: Current Time
import time

current_time = time.asctime()

print(f"Current date and time: {current_time}")

-------------------------------------------------
Exercise 27: Easter Date (Computus Algorithm)

year = int(input("Enter year: "))

a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
month = (h + l - 7 * m + 114) // 31
day = ((h + l - 7 * m + 114) % 31) + 1

print(f"Easter in {year} is on {day}-{month}-{year}")

-------------------------------------------------------
Exercise 28: BMI Calculator

weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

------------------------------------------------------
Exercise 29: Wind Chill

temp = float(input())
wind = float(input())

if temp <= 10 and wind > 4.8:
    wci = 13.12 + 0.6215 * temp - 11.37 * (wind ** 0.16) + 0.3965 * temp * (wind ** 0.16)
    print(f"Wind Chill Index: {round(wci)}")
else:
    print("Invalid input for wind chill calculation.")

-------------------------------------------------------------
Exercise 30: Celsius Conversion
c = float(input())

f = (c * 9/5) + 32
k = c + 273.15

print(f"Fahrenheit: {f:.2f}°F")
print(f"Kelvin: {k:.2f}K")








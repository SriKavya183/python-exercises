Exersice-6- Tax and Tip
meal = float(input("Enter cost of meal: "))
tax = meal * 0.05
tip = meal * 0.18
total = meal + tax + tip
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")

--------------------------------------------------

Exercise-7 Sum of First n Positive Integers
n = int(input("Enter a positive integer: "))
sum_n = (n * (n + 1)) / 2
print("Sum of first", n, "positive integers is", int(sum_n))

-------------------------------------------------------------

Exercise-8- Widgets and Gizmos
widgets = int(input("Enter number of widgets: "))
gizmos = int(input("Enter number of gizmos: "))
weight_widgets = widgets * 75
weight_gizmos = gizmos * 112
total_weight = weight_widgets + weight_gizmos
print("Total weight is", total_weight, "grams")

--------------------------------------------------------------------------

Exercise-9- Compound Interest
deposit = float(input("Enter initial deposit amount: "))
Interest = 0.04
year1 = deposit * (1 + Interest)
year2 = deposit * (1 + Interest) ** 2
year3 = deposit * (1 + Interest) ** 3
print(f"After 1 year: ${year1:.2f}")
print(f"After 2 years: ${year2:.2f}")
print(f"After 3 years: ${year3:.2f}")

-------------------------------------------------------------------

Exercise-10 -Arithmetic
import math
a = int(input("Enter first integer : "))
b = int(input("Enter second integer : "))
sum = a + b
diff = a - b
product = a * b
quotient = a / b
remainder = a % b
log = math.log10(a)
power = a ** b
print(f"Sum: {sum}")
print(f"Difference: {diff}")
print(f"Product: {product}")
print(f"Quotient: {quotient:.2f}")
print(f"Remainder: {remainder}")
print(f"log10(a): {log:.2f}")
print(f"a^b: {power}")

------------------------------------------------------------------

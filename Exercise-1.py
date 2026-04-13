#Exercise-1 Mailing address

print("Kavya Reddy Pagadala")
print("H.No: 11-12-34/1")
print("Street: Street no-11")
print("Area: Gokul Nagar")
print("City: Hyderabad")
print("State: Telangana")
print("PIN Code: 500017")
print("Country: India")


#Exercise-2 Hello Program

name = input("Enter your name: ")
print("Hello", name + "!")

#Exercise 3: Area of a Room

length = float(input(" length of the room (in meters): "))
width = float(input("width of the room (in meters): "))

area = length * width

print(f"The area of the room is {area} square meters.")


#Exercise 4: Area of a Field (in Acres)
length = float(input(" length of the room (in meters): "))
width = float(input("width of the room (in meters): "))

area = length * width
acres = area / 43560

print(f"The area of the field is {acres} acres.")


#Exercise 5: Bottle Deposits

small = int(input(" no of containers (1 liter or less): "))
large = int(input(" no of containers (more than 1 liter): "))

refund = (small * 0.10) + (large * 0.25)

print(f"Total refund: ${refund:.2f}")

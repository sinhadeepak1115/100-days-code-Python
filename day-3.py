from numpy import number

# number = int(input("Which Number Do You Want To Check?"))
#
# if number%2 == 0:
#     print("It is a even number")
# else:
#     print("It is a odd number")

age = int(input("Please Enter Your Age?:"))
height = int(input("What is your Height?:"))
if height > 120:
    if age > 18:
        print("Your eligible for the Roller Ride.")
    else:
        print("Not eligible for the ride.")
elif height <= 120:
    print("Your not eligible.")
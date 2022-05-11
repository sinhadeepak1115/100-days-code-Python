# Rollercoster

height = int(input("What is your Height?:"))

if height >= 120:
    age = int(input("Please Enter Your Age?:"))
    bill = 0

    if age < 12:
        bill = 5

    elif age >= 12 and age <18:
        bill = 7

    elif age >= 18:
        bill = 12

    photo = input("Do you want to take a photo?In Y or N?:")

    if photo == "Y":
        bill +=3
    print(bill)

elif height < 120:
    print("Your not eligible.")
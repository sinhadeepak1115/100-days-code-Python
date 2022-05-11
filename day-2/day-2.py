# day-2 Exercise-1
# two_digit_number = input("Enter a two digit number:")
# total = int(two_digit_number[0]) + int(two_digit_number[1])
# print(total)

# Tip Calculator

print("Welcome to the tip Calculator :)")
bill = float(input("What was the Bill? $"))
# print(bill)
tip_percent = float(input("What percentage was the tip will you like to give?10, 12.5 or 15?"))
# print(tip_percent)
no_people = int(input("No people will split the bill?"))
print(f"Each person should pay {((tip_percent/100*bill)+bill)/no_people}")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height**2)

print(bmi)

if bmi < 18.5:
    print("Your are underwight.")
elif 18.5 <= bmi and bmi < 25:
    print("Your are normal")
elif 25 <= bmi and bmi < 30:
    print("Your are overweight")
elif 30 <= bmi and bmi < 35:
    print("Your are obese")
elif bmi > 35:
    print("Your are clinically obse")
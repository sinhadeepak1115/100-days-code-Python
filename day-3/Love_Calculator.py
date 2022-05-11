# Love Calculator

print("Welcome to Love Calculator!")

name1 = input("Please the name of the first person")
name2 = input("Please the name of the first person")

combine_the_name = name1+name2
lower_case_combine_the_name = combine_the_name.lower()

print(combine_the_name)

t = lower_case_combine_the_name.count("t")
r = lower_case_combine_the_name.count("r")
u = lower_case_combine_the_name.count("u")
e = lower_case_combine_the_name.count("e")

true = t + r + u + e

l = lower_case_combine_the_name.count("l")
o = lower_case_combine_the_name.count("o")
v = lower_case_combine_the_name.count("v")
e = lower_case_combine_the_name.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your Score is {love_score}")
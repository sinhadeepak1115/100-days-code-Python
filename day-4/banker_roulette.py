import random

from numpy import number

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# random_number = random.randint(0, len(names)-1)
# random_person = names[random_number]
# print(random_person)

random_person = random.choice(names)
print(random_person)

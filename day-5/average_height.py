student_heights = input("Inputalist of student heights ").split()
for n in range (0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

total_heights = 0
no_of_people = 0

for height in student_heights:
    total_heights += height
    no_of_people += 1
print(total_heights / no_of_people)
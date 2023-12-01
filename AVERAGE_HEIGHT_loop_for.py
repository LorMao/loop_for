# Input a Python list of student heights
student_heights = [151,145,179]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_student = 0
for student_height in student_heights:
  total_student += student_height
print(f"total height = {total_student}")

how_many = 0
for s in student_heights:
  how_many += 1
print(f"number of students = {how_many}")


for total in student_heights:
  total_average = round(total_student / how_many)
print(f"average height = {total_average}")

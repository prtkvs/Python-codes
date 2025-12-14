marks = [92,91,90,"maths"]
print(marks)
print(marks[2]) # 90
print("-------------------------------------")
print(marks[-1]) # counting from the last
print(marks[-3]) # 91 (third last)
print("-------------------------------------")
print(marks[0:2]) # 92,91 #crazy
print("-------------------------------------")
# loop in array
for score in marks:
    print(score)
print("-------------------------------------")
print(len(marks)) # 4
print("-------------------------------------")
i=0
while i<len(marks):
    print(marks[i])
    i+=1
print("-------------------------------------")
marks.clear() # clears the list
print(marks) # empty
print("--------------Break and Continue-----------------------")

students = ["ram","shyam","radha","tejas","prateek","richa","aditi"]
for student in students:
    if student == "radha":
        break;  # semi colon is optional in python
    print(student)
print("-------------------------------------")
for student in students:
    if student == "radha":
        continue;  # skips radha
    print(student)
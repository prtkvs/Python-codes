marks = (92,91,90,93,93,"english")
# marks[1] = 100  # cannot re-assign as tuples are immutable

print(marks.count(93)) # 2
print(marks.index(93)) # 3

# can represent tuples also as :
roll_no = 1,3,5,12,32
print(roll_no.count(12))
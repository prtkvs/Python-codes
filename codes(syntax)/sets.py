marks = {92,91,90,93,93,"english"} # {} = sets, [] = lists, () = tuples
print(marks) # {'english', 90, 91, 92, 93} -> 93 only 1 time since sets stores unique values
# print(marks[2]) #ERROR - index does not exist in sets

for score in marks:
    print(score)    # unordered : sets are unordered ; same as hashset in java
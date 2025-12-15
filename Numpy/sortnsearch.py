import numpy as np

# Sorting
ar = np.array([7,8,3,4,1])
print(np.sort(ar)) # [1 3 4 7 8]

arr = np.array([[8,3,9],[1,5,2]]) # row wise sorting
print(np.sort(arr))

# Searching
arr2 = np.array([3,4,1,7,8])
print(np.where(arr2 == 4)) # (array([1]),)
print(np.where(arr2 % 2 == 0)) # (array([1, 4]),)

arr3 = np.array([1,4,6,8,9])
print(np.searchsorted(arr3,8)) # 3 ; array must be sorted

# Filter
arr4 = np.array([20,30,40,50])

fa = [True, False, True, False] # fa = filter array
new = arr4[fa]
print(new) # [20 40] ; true value obtained

fa1 = arr4>35 # can do multiple other operations
new = arr4[fa1]
print(new)

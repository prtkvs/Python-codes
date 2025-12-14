# contains 3 types of functions : 1. In-built (studied) 2. Module 3. User-Defined
# Module function
# import math
# print(dir(math)) # for checking all the functions math has

# to use specific function of the module
from math import sqrt
# from math import *    -> to select all functions
print(sqrt(16))


# User-Defined Functions
# syntax : (def = definition)
# def function_name(parameters):
#     // do something

def print_sum(first,second):
    print(first+second)

print_sum(1,2)

# to provide default value to parameter
def print_sum(first,second=4):
    print(first+second)

print_sum(1) # 5 ; default will only used when we dont provide anything on second parameter 
print_sum(1,3) # 4
import numpy as np
import statistics as stats
baked_food = [200,300,150,130,200,280,170,188]

a = np.array(baked_food)
print(np.mean(a)) # average
print(np.median(a)) # sort all then taking the avg of centre; here avg of 188 and 200 since even number of elements
# print(np.mode(a)) # ERROR - since no mode fn in numpy therefore import statistics
print(stats.mode(a)) # 200 since maximum occuring of a number but here occurence of 280 and 200 were same then choose that number which occured first in the array
print(np.std(a)) # represents difference of elements in the array from the mean value, if they are more then std will be more otherwise less values are closer to mean value
print(np.var(a)) # variance - square of std

# Coefficient of Correlation
# -1 = inversely proportional relation
#  0 = no relation
#  1 = directly proportional relation

# understand based on looking to the trend of values increasing or decreasing 
price = [300,100,350,150,200]
sales = [10,20,7,17,3]
print(np.corrcoef([price,sales]))
import numpy as np
a = np.array([20,40,60,70])

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a)) # for count of elements
print(np.mean(a))
print(np.cumsum(a)) 
print(np.cumprod(a))

b = [100,150,199,200]
c = [5,2,5,1]
# b = price of 1, c = quantity
# Determine the price of different total quantities
price = np.array(b)
quantity = np.array(c)
print(np.cumprod([price,quantity],axis =0))


from numpy import *

arr1 = array([
    [1, 2, 3, 4],
    [3, 5, 4, 7]
])

m = matrix("1 2 3; 4 5 6; 7 8 9") 

print(m)
print(diagonal(m))
print(m.min())
print(m.max())
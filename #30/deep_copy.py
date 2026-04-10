from numpy import *

arr1 = array([2, 4, 6, 3, 7])

arr2 = arr1.copy()

arr1[1] = 6 # changed value in both arrays cause view() makes a shallow copy

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
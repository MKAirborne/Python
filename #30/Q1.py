# WAP to add 2 arrays using for loop
from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 4, 3, 2, 1])
arr3 = zeros(5, int)

for i in range(len(arr1)):
    arr3[i] = arr1[i] + arr2[i]

print(arr3) 
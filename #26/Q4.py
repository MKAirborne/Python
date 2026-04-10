# WAP to reverse an array without using in-built function
from numpy import *

arr = array([10, 20, 30, 40, 50])
rev_arr = []

for i in range(len(arr)-1, -1, -1):
    rev_vals = arr[i]

    rev_arr.append(rev_vals)

arr = array(rev_arr)
print(arr)
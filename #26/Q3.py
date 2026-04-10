# create an array with 5 values and delete the value at index number 2 without using in-built function
from numpy import *

arr = array([2, 56, 354, 53, 3])

new_arr = []

for i in range(len(arr)):
    if i != 2:
        new_arr.append(arr[i])

new_arr = array(new_arr)

print(new_arr)



# method 2
# from array import *

# arr = array('i', [10, 20, 30])
# arr.append(40)   # ✅ works!

# print(arr)  # array('i', [10, 20, 30, 40])
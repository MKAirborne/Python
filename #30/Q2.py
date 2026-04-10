# WAP to find the max value from an array without using in-built functions
from numpy import *

arr = array(['v', 'l', 'o', 'a', 'n'])

max_val = arr[0]
for i in arr:

    if i >= max_val:
        max_val = i

print(max_val)
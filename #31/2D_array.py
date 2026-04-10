from numpy import *

arr1 = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 1]
])


# print(arr1.dtype)   #--> give type of stored data
# print(arr1.ndim)    #--> gives dimension of array
# print(arr1.shape)   #--> gives shape of array
# print(arr1.size)    #--> gives size of array

arr2 = arr1.flatten()   #--> Multi-D to 1D 

arr3 = arr1.reshape(2, 2, 3)

print(arr3)
print(arr3.ndim)

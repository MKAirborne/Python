from numpy import *

arr = array([10, 20, 30, 40, 50])
new_arr = []

for i in range(len(arr)):
    if i != 2:
        new_arr.append(arr[i])

print(new_arr)  # have the property of numpy after appended
# [np.int64(10), np.int64(20), np.int64(40), np.int64(50)]
# solution .append(int(arr[i]))
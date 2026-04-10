from numpy import *

arr = logspace(1, 40, 5)

print('%.2f' %arr[0])
print('%.2f' %arr[1])
print('%.2f' %arr[2])
print('%.2f' %arr[3])
print('%.2f' %arr[4])

# Syntax (NumPy)
# numpy.logspace(start, stop, num=50, base=10.0)

# start   --> Exponent of the first value: base^start
# stop  --> Exponent of the last value: base^stop
# num   --> How many values to generate
# base  --> The base of the logarithm (default: 10)
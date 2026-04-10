from array import *

vals = array('i', [4, 2, 5, 11, 6])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)
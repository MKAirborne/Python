for i in []:
    print(i)
else:
    print("Empty")



x = [1,2,3]
for i in x:
    x.remove(i)
print(x)



print([i for i in range(5) if i % 2])
# [ expression   for variable in sequence   if condition ]
#       i           for i     in range(5)   if i % 2
a = 10
print(id(a))

def something():
    
    a = 9
    print("In fun", a)

    x = globals()['a']
    print(id(x))
    globals()['a'] = 15


something()

print("Outside", a)
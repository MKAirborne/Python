a = 10

def something():
    global a
    a = 15
    print("in Function ", a)

something()


print("outside",a)
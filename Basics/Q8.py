a = (1, 2, 3)
print("a id:", id(a))

b = a
print("b id:", id(b))

a = a + (3,)
print("new a id:", id(a))
print("b id still:", id(b))
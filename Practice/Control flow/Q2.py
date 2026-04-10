print(all([True, False, True]))


print(any([True, False, True]))


all([])   # True  ← "all zero elements satisfy the condition" (vacuous truth)
any([])   # False ← "no elements exist to be True"

x = 5
print("Even" if x % 2 == 0 else "Odd")
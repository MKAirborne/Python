x = 5
print(x is 5)

# Why x is 5 is True (but you shouldn't rely on it)
# Output
# pythonx = 5
# print(x is 5)  # True  (but may show a SyntaxWarning in Python 3.8+)

# First — is vs ==, What's the Difference?
# python==   → checks VALUE equality      (do they have the same value?)
# is   → checks IDENTITY equality   (do they point to the same object in memory?)
# pythonx = 5
# print(x == 5)  # True  ← values are equal
# print(x is 5)  # True  ← SAME object in memory (why?)

# The Core Reason: Integer Caching (Small Int Cache)
# CPython (the standard Python interpreter) pre-creates and caches integer objects for small numbers in the range:
# -5  to  256
# These objects are created once at startup and reused everywhere. So instead of creating a new object every time you write 5, Python just reuses the same cached object.
# pythonx = 5   # x points to cached object at, say, address 0x100
# 5       # this literal also points to the SAME cached address 0x100

# x is 5  # True ← both point to identical memory address!

# What Happens OUTSIDE the Cache Range (> 256)?
# pythonx = 257
# print(x is 257)   # False ← outside cache, new objects created each time!

# a = 1000
# b = 1000
# print(a is b)     # False ← two separate objects in memory
# print(a == b)     # True  ← but values are equal
# a = 1000  →  a ──→ 0x200  (new object)
# b = 1000  →  b ──→ 0x300  (another new object)

# a is b  →  0x200 == 0x300  →  False ❌
# a == b  →  1000  == 1000   →  True  ✅

# Verify the Cache Yourself
# python# Inside cache range (-5 to 256)
# a = 100
# b = 100
# print(a is b)   # True  ← same cached object
# print(id(a) == id(b))  # True ← identical memory address

# # Outside cache range
# a = 1000
# b = 1000
# print(a is b)   # False ← different objects
# print(id(a), id(b))  # different memory addresses

# Python 3.8+ Warning
# From Python 3.8 onwards, using is with literals throws a SyntaxWarning:
# pythonx = 5
# print(x is 5)
# # SyntaxWarning: "is" with a literal. Did you mean "=="?
# Python is telling you — don't use is for value comparison!

# # ✅ Correct usage of 'is'
# x = None
# print(x is None)   # True — correct way to check None

# # ❌ Wrong usage of 'is'
# x = 5
# print(x is 5)      # Unreliable — works by accident due to caching
# print(x is "hello") # Unreliable — string interning, not guaranteed

# Bottom line: x is 5 is True only because of CPython's internal integer caching for -5 to 256. It's an implementation detail, not a language guarantee. Always use == for value comparison.

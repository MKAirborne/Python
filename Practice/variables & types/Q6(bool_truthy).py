print(bool(""), bool(" "))

# Why bool("") is False but bool(" ") is True
# Output
# pythonprint(bool(""), bool(" "))  # False True

# The Core Reason: Python's Truthiness Rules
# Python determines the boolean value of an object based on truthiness (truthy/falsy) rules, not just its type.
# For strings, the rule is simple:

# ✅ A string is True if it has at least one character (even a space)
# ❌ A string is False only if it is completely empty ""


# The Key Difference
# python""   → length = 0  → Falsy → False
# " "  → length = 1  → Truthy → True
# A space " " is a valid character in Python. It is not nothing — it occupies memory and has a length of 1.
# pythonlen("")   # 0  ← empty, no characters
# len(" ")  # 1  ← has ONE character (a space)

# How Python Evaluates Truthiness Internally
# Python calls __bool__() or __len__() under the hood:
# python"".__len__()   # 0  → bool(0) → False
# " ".__len__()  # 1  → bool(1) → True
# If __len__ returns 0 → object is Falsy.
# If __len__ returns anything non-zero → object is Truthy.

# More String Truthiness Examples
# pythonbool("")          # False  ← empty string
# bool(" ")         # True   ← single space
# bool("  ")        # True   ← multiple spaces
# bool("\n")        # True   ← newline is a character
# bool("\t")        # True   ← tab is a character
# bool("False")     # True   ← non-empty string, even "False"!
# bool("0")         # True   ← "0" is a character, not the number 0

# ⚠️ bool("False") and bool("0") are both True — because they are non-empty strings!


# Complete Python Falsy Values (for reference)
# pythonbool("")          # False  ← empty string
# bool(0)           # False  ← zero int
# bool(0.0)         # False  ← zero float
# bool([])          # False  ← empty list
# bool({})          # False  ← empty dict
# bool(())          # False  ← empty tuple
# bool(set())       # False  ← empty set
# bool(None)        # False  ← None

# Everything else in Python is Truthy ✅


# Practical Use Case
# pythonuser_input = " "

# # ❌ Wrong way — space passes as valid input!
# if user_input:
#     print("Input received")   # This runs even for blank spaces!

# # ✅ Correct way — strip whitespace first
# if user_input.strip():
#     print("Input received")   # Won't run for spaces-only input
# else:
#     print("Empty input!")     # This runs correctly

# The Golden Rule

# A string is False only when it is exactly "" (zero characters).
# Any string with even a single whitespace is True.
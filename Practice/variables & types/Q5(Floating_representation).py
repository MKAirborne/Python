print(0.1 + 0.2 == 0.3)

# The Core Reason: Floating Point Representation
# Computers store numbers in binary (base-2), but 0.1, 0.2, and 0.3 cannot be represented exactly in binary — just like 1/3 cannot be represented exactly in decimal (0.3333...).

# Decimal vs Binary Analogy
# 1/3 in decimal  →  0.3333333...  (infinite, inexact)
# 0.1 in binary   →  0.0001100110011001100...  (infinite, inexact)
# Since memory is finite, Python rounds these at the 64-bit boundary, introducing tiny errors.

# What Python Actually Stores
# pythonfrom decimal import Decimal

# print(Decimal(0.1))  # 0.1000000000000000055511151231257827021181583404541015625
# print(Decimal(0.2))  # 0.200000000000000011102230246251565404236316680908203125
# print(Decimal(0.3))  # 0.299999999999999988897769753748434595763683319091796875

# So when you add 0.1 + 0.2:
# python0.1  →  0.1000000000000000055511...
# 0.2  →  0.2000000000000000111022...
#      ─────────────────────────────
# sum  →  0.3000000000000000444089...  ← slightly MORE than 0.3

# 0.3  →  0.2999999999999999888977...  ← slightly LESS than 0.3

# Seeing the Actual Difference
# pythonprint(0.1 + 0.2)        # 0.30000000000000004  ← not exactly 0.3
# print(0.1 + 0.2 == 0.3) # False
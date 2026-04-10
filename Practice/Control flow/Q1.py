x = 5
if x > 2:
    print("A")
elif x > 3:
    print("B")



y = 0
if y:
    print("Yes")
else:
    print("No")



for i in range(3):
    print(i)
else:
    print("Done")
#     The Core Reason: for-else is a Python Feature
# In Python, else on a loop does not mean "if the loop didn't run".
# It means:

# ✅ "Run this block when the loop finishes NORMALLY (without being interrupted)"



for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Done")
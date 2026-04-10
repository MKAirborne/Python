# 1 2 3 4
# 2 3 4
# 3 4 
# 4

i = 1

while(i <= 4):
    j = i
    while(j <= 4):
        print(j, end=" ")
        j += 1
    print()
    i += 1


for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()

# A P Q R
# A B Q R
# A B C R
# A B C D   

for i in range(4):

    for j in range(i+1):
        print(chr(ord("A")+j), end=" ")

    for k in range(3-i):
        print(chr(ord("P")+k), end=" ")
    print()

    i += 1
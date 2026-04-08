# for i in range(1, 501):
#     root = int(i ** 0.5)
#     if root * root == i:
#         print(i)


# Best solution
n = 1
while n * n <= 500:
    print(n * n)
    n += 1
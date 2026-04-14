def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1

    return even, odd

lst = [20, 45, 46, 57, 78, 36, 23, 45, 56]

even, odd = count(lst)

print(even, odd)
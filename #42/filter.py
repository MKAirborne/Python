def is_even(n):
    return n%2==0

nums = [2, 3, 4, 6, 4, 5, 7, 9, 8, 6, 2]

evens = list(filter(is_even, nums))

print(evens)
nums = [2, 3, 4, 6, 4, 5, 7, 9, 8, 6, 2]

evens = list(filter(lambda n : n%2==0, nums))

doubles = list(map(lambda n : n*2, evens))

print(doubles)
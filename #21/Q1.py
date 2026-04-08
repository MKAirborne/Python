# Print all perfect squares between 1 to 500

for i in range(1, 501):
    if (i ** 0.5).is_integer():
        print(i)
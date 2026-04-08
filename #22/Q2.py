n = int(input("Enter a number:"))

if n <= 1:
    print("not a prime number")

else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("not a prime number")
            break
        else:
            print("prime number")
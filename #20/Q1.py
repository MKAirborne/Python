# WAP to print all values from 1 to 100 and skip the numbers which are divisible by 3 or 5

n = 1

while(n <= 100):
    if((n % 3  != 0) and (n % 5 != 0)):
        print(n)
    n += 1
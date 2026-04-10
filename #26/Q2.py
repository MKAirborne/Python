#  write a code to find factorial of a given number

num = int(input("Enter a number:"))


result = 1
for i in range(1, num+1):
    if(num <= 0):
        print("enter number greater than 0")

    else:
        result *= i

print("Factorial of given number is ", result)
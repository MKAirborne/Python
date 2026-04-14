# mainly two types of arguments, 1) Formal, 2)Actual
# def update(a, b): --> here a and b are formal arguments
# update(5, 6) --> here 5, 6 are actual arguments
# There are 4 types of actual arguments
# 1) positional: (a, b) --> (5, 6)
# 2) keyword : (name, age) --> (name='mayank', age= 21)
# 3) default : (name, age=18) but we pass ('Mayank')

# 4) variable length
def sum(a, *b):
    print(type(b))
    c = a

    for i in b:
        c = c + i
    print(c)

sum(5, 6, 76, 100)
def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)

person('Mayank', age = 21, city = 'Dhoraji', mob = 87330)
# Code without EAFP
def example_1():
    print('Type a positive integer(defaults to 1)')
    if (s := input(">> ")).isnumeric():
        return int(s)
    return 1


# Code with EAFP approach
def example_2():
    print('Type a positive integer(defaults to 1)')
    try:
        return int(input(">> "))
    except ValueError:
        return 1


# Code with EAFP approach
def example_3():
    d = {'a': 1, 'b': 2}
    print('What key do you want to access?')
    try:
        return d[key := input('>> ')]
    except KeyError:
        return f'Cannot find key: {key}'


# Code with EAFP approach
def example_4():
    print('What file do I read?')
    try:
        with open(filepath := input('>> '), 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        return f'Woops, the file: {filepath} does not exist'
    else:
        print('Do something with contents...')
        ...


print(example_4())

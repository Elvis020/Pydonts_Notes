# without walrus
import re
import sys
from math import factorial

a = 3
print(a)

# print(b = 3) # Not possible

# With walrus
print(b := 12)  # with walrus, you can assign and use on the same line

# if (i := input())[0] == 'q' or i == 'exit':
#     sys.exit()


# Context 1
# Without walrus(in while loops)
inp = input()
while inp:
    eval(inp)
    inp = input()

# With walrus(in while loops)
while inp := input(' >> '):
    eval(inp)


# Context 2
# Without walrus
def trailing_zeros(n):
    s = str(n)
    return len(s) - len(s.rstrip('0'))


# With walrus
def trailing_zeros_2(n):
    return len(s := str(n)) - len(s.rstrip('0'))


# Context 3
# Without walrus
l = [3, 17, 89, 15, 58, 193]
facts = [factorial(num) for num in l if trailing_zeros(factorial(num) > 50)]

# With walrus
facts_2 = [f for num in l if trailing_zeros(f := factorial(num) > 50)]

# This is for efficiency in the context of the function we are using and not related to walrus
facts_4 = [num for num in map(factorial, l) if trailing_zeros_2(num) > 50]


# Context 4
# Without walrus
string = input('Your contact info: >> ')
email = re.search(r'\b(\w+@\w+\.com)\b', string)
if email:
    print(f'Your email is {email.group(1)}')
else:
    phone = re.search(r'\d{9}',string)
    if phone:
        print(f'Your phone is {phone.group(1)}')
    else:
        print('No info found...')

# With walrus
string = input('Your contact info: >> ')
if email := re.search(r'\b(\w+@\w+\.com)\b', string):
    print(f'Your email is {email.group(1)}')
elif phone := re.search(r'\d{9}',string):
    print(f'Your phone is {phone.group(1)}')
else:
    print('No info found...')
lst = [0, 1, 2, 3, 4]

head, *tail = lst
print(head)
print(tail)
print()
string = "Hello!"
*start, last = string
print(start)
print(last)
print()
a, b, *c, d = range(5)
print(b)
print(c)
print(d)
print()
print("Credit Card Checker using Luhn's algorithm")


def verify_check_digit(digits):
    """Use Luhn's algorithm to verify check digit"""
    # *digits, check_digit = digits
    weight = 2
    acc = 0
    for digit in reversed(digits[:-1]):
        value = digit * weight
        acc += (value // 10) + (value % 10)
        weight = 3 - weight
    return (9 * acc % 10) == digits[-1]


assert verify_check_digit([7, 9, 9, 2, 7, 3, 9, 8, 7, 1, 3]) == True

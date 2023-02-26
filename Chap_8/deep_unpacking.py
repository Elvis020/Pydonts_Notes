rgb_values = (111, 123, 45)
a, b, c = rgb_values
print(a, b, c, sep=',')

nums = [0, 1, 2, 3, 4]
# head, *body = l
# print(head, body)
head, *body, tail = nums
print(f'{head=}, {tail=}, {body=}')

# Nested iterables
print()
colour_info = ('AliceBlue', (240, 248, 255))
name, (r, g, b) = colour_info
print(f'{name=}, {r=},{g =},{b=}')

# In for-loops
scores = [('Elvis', (1, 2, 3)), ('Kelvin', (4, 5, 6)), ('Ama', (7, 8, 9))]
print([name for name, (a, b, c) in scores])

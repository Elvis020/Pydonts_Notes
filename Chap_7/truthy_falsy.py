assert bool([]) is False
assert bool('') is False


# class A:
#     ...
#
#
# a = A()
# if a:
#     print('Hello World')
#
#
# class B:
#     def __bool__(self):
#         return False
#
#
# b = B()
# if b:
#     print('B works the same as A')

class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point2D({repr(self.x)}, {repr(self.y)})'

    def __bool__(self):
        return bool(self.x or self.y)


print(bool(Point2D(0, 1)))
print(bool(Point2D(0, 0)))
print(bool(Point2D(1, 0)))
print(bool(Point2D(4, 2)))
print(Point2D(4, 2))
# str and repr
import datetime

print(3)
print("3")


class A:
    def __str__(self):
        return "A"


a = A()
print()
print(a)

print()

date = datetime.datetime(2023, 2, 2)
print(repr(date))  # uses repr
print(date)  # uses str(just creates a nice-looking representation)

print()


class Point2D:
    """A class to represent points in a 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Provides a good-looking representation of the object"""
        return f"({self.x},{self.y})"

    def __repr__(self):
        """Provides an unambiguous way of rebuilding this object"""
        return f"Point2D({repr(self.x)},{repr(self.y)})"


p = Point2D(0, 0)
print(f"To build the point {p} in your code, try writing {repr(p)}")

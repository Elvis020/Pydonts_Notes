# Structural pattern matching
colors = (25, 56, 200)

match colors:
    case r, g, b:
        print("No alpha")
    case r, g, b, alpha:
        print(f"Alpha is {alpha}")


# factorial with if-else
def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


# factorial with match-case
def fac_with_match_case(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * fac_with_match_case(n - 1)


class Point2D:
    """A class to represent points in a 2D space."""

    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Provides a good-looking representation of the object"""
        return f"({self.x},{self.y})"

    def __repr__(self):
        """Provides an unambiguous way of rebuilding this object"""
        return f"Point2D({repr(self.x)},{repr(self.y)})"


# without __match_args__
# def describe_point(point):
#     match point:
#         case Point2D(x=0, y=0):
#             desc = "at origin"
#         case Point2D(x=0, y=y):
#             desc = f"in the vertical axis, at y={y}"
#         case Point2D(x=x, y=0):
#             desc = f"in the horizontal axis, at x={x}"
#         case Point2D(x=x, y=y) if x == y:
#             desc = f"along the x = y line, with x = y = {x}"
#         case Point2D(x=x, y=y) if x == -y:
#             desc = f"along the x = -y line, with x = {x} and  y = {y}"
#         case Point2D(x=x, y=y):
#             desc = f"at {point}"
#     return f"The point is {desc}"


# with __match_args__ and matching structure of objects
def describe_point(point):
    match point:
        case Point2D(0, 0):
            desc = "at origin"
        case Point2D(0, y):
            desc = f"in the vertical axis, at y={y}"
        case Point2D(x, 0):
            desc = f"in the horizontal axis, at x={x}"
        case Point2D(x, y) if x == y:
            desc = f"along the x = y line, with x = y = {x}"
        case Point2D(x, y) if x == -y:
            desc = f"along the x = -y line, with x = {x} and  y = {y}"
        case Point2D(x, y):
            desc = f"at {point}"
    return f"The point is {desc}"


# print(fac(5))
# print(fac_with_match_case(5))
print(describe_point(Point2D(0, 0)))
print(describe_point(Point2D(3, 0)))
print(describe_point(Point2D(3, -3)))

# Plain dictionary matching
dictty = {0: "oi", 1: "uno"}
match dictty:
    case {0: "oi"}:
        print("yeah")
match dictty:
    case {0: "oi", **remainder}:
        print("Hell yeah")


# Naming sub-patterns

# Simple case
def go(direction):
    match direction:
        case "North" | "West" | "East" | "South":
            print('Alright, I am going...')
        case _:
            print("I can't go that way.")


# Complex nested cases
def act(command):
    match command.split():
        case "Cook", "breakfast":
            print("I love breakfast")
        case "Cook", *whatever:
            print("Cooking...")
        case "Go", "North" | "East" | "West" | "South" as direction:
            print(f"Alright, I am going {direction}")
        case "Go", *wherever:
            print("I can't go that way...")
        case _:
            print("I can't do that")


print()
go('North')
go('adds adjaksd')

print()
act('Go North')
act('Go adds adjaksd')
act('Cook breakfast')
act('Drive')
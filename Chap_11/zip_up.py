# zip in action
from pathlib import PurePath

first = ["Anna", "Bob", "Charles"]
last = ["Smith", "Doe", "Evans"]
last2 = ["Smith", "Doe", "Evans", "Elvis"]
for firsts, lasts in zip(first, last):
    print(f"{firsts} {lasts}")

# Pathlib implements zip in its implementation
assert True == PurePath("a/b.py").match("*.py")
assert True == PurePath("a/b/c.py").match("b/*.py")
assert False == PurePath("a/b/c.py").match("a/*.py")

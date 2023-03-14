from itertools import chain


def flatten_a_list(lst):
    """This simply flattens a list on level deep"""
    return list(chain(*lst))


def flatten_a_list_2(lst):
    """Another way of flattening a list on level deep"""
    return sum(lst, [])


print(flatten_a_list([[1, 2, 3], [4], [5, 6]]))
print(flatten_a_list_2([[1, 2, 3], [4], [5, 6]]))

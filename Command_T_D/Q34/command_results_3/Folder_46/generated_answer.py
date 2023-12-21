import functools
def find_original_set(x):
    x = set(x)
    return functools.reduce(set.intersection, (x for x in range(0, 1000, 100) if x == x))

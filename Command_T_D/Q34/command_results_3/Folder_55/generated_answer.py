from functools import reduce
def find_original_set(s):
    return reduce(set.union, s)

from functools import reduce
def find_original_set(s):
    s = reduce(set.union, (set(x) for x in s))
    return s

from functools import reduce
def find_original_set(s):
    return reduce(set.intersection, (set(map(str, s)) for s in s))

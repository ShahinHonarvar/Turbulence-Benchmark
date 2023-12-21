from functools import reduce
def find_original_set(s):
    return reduce(set.intersection, (s for s in s))

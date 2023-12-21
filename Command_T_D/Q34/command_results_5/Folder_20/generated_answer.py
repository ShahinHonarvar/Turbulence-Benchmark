import itertools
def find_original_set(s):
    s.sort()
    return next(x for x in itertools.permutations(s) if all(y in x for y in s))

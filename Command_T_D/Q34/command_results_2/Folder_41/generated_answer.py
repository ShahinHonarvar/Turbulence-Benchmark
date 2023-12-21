import itertools
def find_original_set(s):
    return next(s for s in itertools.permutations(range(1, 21), 20) if all(x in s for x in s))

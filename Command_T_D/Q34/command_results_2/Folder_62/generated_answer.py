import itertools
def find_original_set(s):
    return next(x for x in itertools.permutations(range(790), 790) if set(x) == set(s))

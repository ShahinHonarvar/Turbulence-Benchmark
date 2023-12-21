import itertools
def find_original_set(S):
    return next(x for x in itertools.permutations(S) if set(x) == S)

import itertools
def find_original_set(s):
    return set.intersection(*map(set, itertools.permutations(s)))

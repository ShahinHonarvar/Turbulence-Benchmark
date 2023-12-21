import itertools
def find_original_set(s):
    s = set(s)
    sets = set(itertools.combinations(s, 2))
    sets |= set(itertools.permutations(s))
    return sets

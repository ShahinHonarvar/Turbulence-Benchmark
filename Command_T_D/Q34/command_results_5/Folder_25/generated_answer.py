import itertools
def find_original_set(s):
    sets = set(s)
    return set.intersection(*[set(x) for x in itertools.permutations(sets)])

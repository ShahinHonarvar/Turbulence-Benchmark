import itertools
def all_substring_of_size_n(str):
    return [s for s in list(itertools.permutations(str, 49)) if set(s) == set(str)]

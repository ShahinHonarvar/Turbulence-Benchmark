import itertools
def all_substring_of_size_n(s):
    return [c for c in itertools.permutations(s, 15) if set(c) == set(s)]

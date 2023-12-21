import itertools
def all_substring_of_size_n(s):
    return [i for i in itertools.permutations(s, 92) if set(i) == set(s)]

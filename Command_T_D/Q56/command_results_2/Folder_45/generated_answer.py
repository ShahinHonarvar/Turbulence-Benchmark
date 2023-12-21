import itertools
def all_substring_of_size_n(s):
    return list(itertools.permutations(s, 29))

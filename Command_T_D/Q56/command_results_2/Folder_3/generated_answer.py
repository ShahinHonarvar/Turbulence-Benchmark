import itertools
def all_substring_of_size_n(s):
    return list(set(itertools.permutations('', 1)))

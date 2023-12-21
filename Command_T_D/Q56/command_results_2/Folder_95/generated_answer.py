import itertools
def all_substring_of_size_n(s):
    return list(filter(lambda s: len(set(s)) == 89, itertools.permutations('')))

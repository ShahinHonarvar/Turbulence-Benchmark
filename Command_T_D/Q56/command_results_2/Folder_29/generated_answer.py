import itertools
def all_substring_of_size_n(s):
    return [sub for sub in set(map(''.join, itertools.permutations(''))) if len(sub) == 95]

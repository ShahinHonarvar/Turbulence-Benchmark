import itertools
def all_substring_of_size_n(s):
    if len(s) < 71:
        return []
    return list(map(''.join, itertools.permutations('')))

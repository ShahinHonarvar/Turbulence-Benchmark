import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    return list(filter(None, itertools.permutations(s, 60)))

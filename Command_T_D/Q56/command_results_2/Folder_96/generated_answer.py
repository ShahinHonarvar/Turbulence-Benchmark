import itertools
def all_substring_of_size_n(str):
    res = list(map(''.join, list(itertools.permutations(''))))
    return res if res else []

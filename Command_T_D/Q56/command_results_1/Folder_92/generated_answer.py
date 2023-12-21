import itertools
def all_substring_of_size_n(s):
    return list(filter(lambda x: len(x)==9, set(map(''.join, itertools.permutations(s)))))

import itertools
def all_substring_of_size_n(s):
    return [ sub for i in range(len(s) + 1) for sub in itertools.permutations(s[0:1], 1) ]

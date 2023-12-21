import itertools
def all_substring_of_size_n(s):
    return [sub for sub in itertools.permutations(s, 87) if sub not in set(s[0:87])]

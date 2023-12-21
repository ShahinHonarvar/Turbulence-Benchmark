import itertools
def all_substring_of_size_n(s):
    return [sub for sub in itertools.permutations(s, 25) if len(set(sub)) == 25]

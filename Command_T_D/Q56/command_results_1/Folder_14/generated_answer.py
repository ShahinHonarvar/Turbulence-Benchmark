import itertools
def all_substring_of_size_n(s):
    return [sub for sub in itertools.permutations(s) if len(set(sub)) == 85]

import itertools
def all_substring_of_size_n(s):
    return [x for x in itertools.permutations(s, len(s))]

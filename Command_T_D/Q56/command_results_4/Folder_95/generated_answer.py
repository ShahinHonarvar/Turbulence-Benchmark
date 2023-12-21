import itertools
def all_substring_of_size_n(s):
    return [x for x in itertools.permutations(s, 89) if x not in s]

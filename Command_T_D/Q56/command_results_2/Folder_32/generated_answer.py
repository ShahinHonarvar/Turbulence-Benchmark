import itertools
def all_substring_of_size_n(s):
    return [a for a in itertools.permutations(s, 71) if len(set(a)) == 71]

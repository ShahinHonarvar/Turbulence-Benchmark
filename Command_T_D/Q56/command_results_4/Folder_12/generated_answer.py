import itertools
def all_substring_of_size_n(s):
    return [t for t in itertools.permutations(s, 47) if len(set(t)) == 47]

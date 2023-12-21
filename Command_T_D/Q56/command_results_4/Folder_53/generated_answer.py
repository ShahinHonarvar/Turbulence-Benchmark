import itertools
def all_substring_of_size_n(s):
    return [x for x in itertools.permutations(s, len(x)) if len(x) == 25 and len(set(x)) == 25]

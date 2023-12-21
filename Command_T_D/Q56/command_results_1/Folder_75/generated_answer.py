import itertools
def all_substring_of_size_n(str):
    return [x for x in itertools.permutations(str, 16) if len(set(x)) == 16]

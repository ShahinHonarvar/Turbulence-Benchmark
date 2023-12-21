import itertools
def all_substring_of_size_n(str):
    return [s for s in itertools.permutations(str, 85) if len(set(s)) == 85]

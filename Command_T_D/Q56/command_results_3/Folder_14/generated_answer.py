import itertools
def all_substring_of_size_n(s):
    return [t for t in itertools.permutations('') if len(t)==85]

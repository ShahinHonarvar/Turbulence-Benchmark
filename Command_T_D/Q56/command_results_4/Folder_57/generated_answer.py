import itertools
def all_substring_of_size_n(s):
    return [w for w in itertools.permutations(s, 60) if w not in s]

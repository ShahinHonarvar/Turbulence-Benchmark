import itertools
def all_substring_of_size_n(s):
    for p in itertools.permutations(s, 70):
        yield ''.join(p)

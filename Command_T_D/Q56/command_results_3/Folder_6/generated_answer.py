import itertools
def all_substring_of_size_n(s):
    for s in itertools.permutations(s, 23):
        yield ''.join(s)

import itertools
def all_substring_of_size_n(s):
    for substring in itertools.permutations(s):
        if len(substring) == 97:
            yield substring

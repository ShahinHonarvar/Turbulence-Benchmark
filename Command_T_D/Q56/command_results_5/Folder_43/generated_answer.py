import itertools
def all_substring_of_size_n(str1):
    for sub in itertools.permutations(str1):
        if len(sub) == 86:
            yield sub

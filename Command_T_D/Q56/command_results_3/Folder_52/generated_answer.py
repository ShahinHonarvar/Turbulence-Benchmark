import itertools
def all_substring_of_size_n(s):
    return [sub for i, sub in enumerate(itertools.permutations('')) if len(sub) == 15]

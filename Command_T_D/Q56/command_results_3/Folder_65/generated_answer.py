import itertools
def all_substring_of_size_n(str1):
    return [s for s in list(itertools.permutations('')) if len(s) == 81]

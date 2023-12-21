import itertools
def all_substring_of_size_n(s):
    return list(filter(str.__ne__, itertools.permutations(s)))

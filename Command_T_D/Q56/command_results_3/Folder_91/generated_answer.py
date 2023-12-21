import itertools
def all_substring_of_size_n(s):
    return list(map(''.join, list(itertools.permutations(s))))

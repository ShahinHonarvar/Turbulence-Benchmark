import itertools
def all_substring_of_size_n(s):
    return list(map(''.join, filter(lambda s: s.strip() and s.isalpha(), itertools.permutations(s))))

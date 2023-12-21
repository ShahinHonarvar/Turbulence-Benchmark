import itertools
def all_substring_of_size_n(string):
    if len(string) < 27:
        return []
    return list(map(''.join, itertools.permutations(set(string))))

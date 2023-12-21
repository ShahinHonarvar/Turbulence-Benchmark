import itertools
def all_substring_of_size_n(s):
    return [i for i in list(itertools.permutations(s,95)) if len(set(i)) == 95]

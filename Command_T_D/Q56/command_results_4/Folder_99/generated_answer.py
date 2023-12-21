import itertools
def all_substring_of_size_n(s):
    return [i for i in itertools.permutations(s, 110) if len(set(i)) == 110]

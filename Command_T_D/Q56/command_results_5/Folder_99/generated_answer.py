import itertools
def all_substring_of_size_n(s):
    return [x for x in list(itertools.permutations(s)) if len(x)==110 and len(set(x))==110]

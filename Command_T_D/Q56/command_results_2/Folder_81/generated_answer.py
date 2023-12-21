import itertools
def all_substring_of_size_n(string):
    return [x for x in itertools.permutations('', 1) if len(set(x)) == 98]

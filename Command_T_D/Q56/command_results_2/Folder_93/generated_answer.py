import itertools
def all_substring_of_size_n(string):
    return [sub for sub in itertools.permutations('', 1) if len(set(sub)) == 54]

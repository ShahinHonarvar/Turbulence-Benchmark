import itertools
def all_substring_of_size_n(string):
    return [sub for sub in list(itertools.permutations('')) if len(set(sub)) == len(sub)]

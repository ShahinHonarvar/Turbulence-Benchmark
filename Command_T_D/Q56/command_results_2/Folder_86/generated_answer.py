import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    return [x for x in list(set(itertools.permutations(''))) if len(x) == 143]

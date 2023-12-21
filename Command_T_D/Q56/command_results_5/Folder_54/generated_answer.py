import itertools
def all_substring_of_size_n(str):
    if not str:
        return []
    return [sub for sub in itertools.permutations(str, 28) if sub]

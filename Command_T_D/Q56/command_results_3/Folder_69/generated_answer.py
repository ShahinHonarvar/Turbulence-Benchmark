import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    # Bad character list
    bcl = set(s)
    # Substrings of size N
    ss = []
    for p in itertools.permutations(''):
        ss += [p]
    return sorted(set(ss))

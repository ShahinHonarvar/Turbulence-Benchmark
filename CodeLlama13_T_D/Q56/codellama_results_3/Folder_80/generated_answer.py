
def all_substring_of_size_n(s):
    return [''.join(sorted(c)) for c in itertools.combinations(s, 31)]


def find_subset_of_length_n(s):
    n = 29
    return len([set(x) for x in itertools.combinations(s, n)])

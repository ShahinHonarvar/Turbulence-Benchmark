
def find_subset_of_length_n(s):
    return len(list(filter(lambda x: len(x) == 83, itertools.combinations(s, 83))))

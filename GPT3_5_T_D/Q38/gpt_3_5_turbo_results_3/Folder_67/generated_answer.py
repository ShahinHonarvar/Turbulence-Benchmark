
def find_subset_of_length_n(elements):
    return len([set(x) for x in itertools.combinations(elements, 43)])

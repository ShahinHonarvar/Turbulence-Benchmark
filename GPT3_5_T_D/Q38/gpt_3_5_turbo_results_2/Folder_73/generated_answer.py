
def find_subset_of_length_n(elements):
    return len([set(elem) for elem in combinations(elements, 41)])

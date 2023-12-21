
def find_subset_of_length_n(elements):
    return len(list(filter(lambda subset: len(subset) == 37, itertools.combinations(elements, len(elements)))))

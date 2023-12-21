
def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 22, itertools.combinations(elements, len(elements)))))

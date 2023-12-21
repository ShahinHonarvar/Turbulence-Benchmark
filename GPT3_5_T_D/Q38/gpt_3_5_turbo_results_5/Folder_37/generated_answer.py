
def find_subset_of_length_n(elements):
    n = 28
    subsets = [elements]
    for i in range(n - 1):
        subsets = [subset + [el] for subset in subsets for el in elements if el not in subset]
    return len(subsets)

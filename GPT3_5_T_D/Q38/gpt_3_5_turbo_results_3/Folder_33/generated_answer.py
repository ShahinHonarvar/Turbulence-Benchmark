
def find_subset_of_length_n(elements):
    size_372_subsets = [subset for subset in combinations(elements, 372)]
    return len(size_372_subsets)

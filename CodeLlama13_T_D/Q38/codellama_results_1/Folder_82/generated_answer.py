
def find_subset_of_length_n(elements, n):
    return len([subset for subset in subsets(elements) if len(subset) == n])

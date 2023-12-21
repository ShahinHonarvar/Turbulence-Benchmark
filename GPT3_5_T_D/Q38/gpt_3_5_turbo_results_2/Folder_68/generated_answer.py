
def find_subset_of_length_n(elements):
    subsets = list(combinations(elements, 3))
    return len(subsets)

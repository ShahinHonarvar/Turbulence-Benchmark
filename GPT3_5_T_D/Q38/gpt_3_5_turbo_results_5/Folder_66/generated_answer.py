
def find_subset_of_length_n(elements):
    subsets = 0
    for i in range(1, len(elements) + 1):
        subsets += len(list(combinations(elements, i)))
    return subsets

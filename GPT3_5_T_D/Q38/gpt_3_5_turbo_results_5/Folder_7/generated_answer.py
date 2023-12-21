
def find_subset_of_length_n(elements):
    num_subsets = 0
    for i in range(1, len(elements)+1):
        num_subsets += len(list(combinations(elements, i)))
    return num_subsets

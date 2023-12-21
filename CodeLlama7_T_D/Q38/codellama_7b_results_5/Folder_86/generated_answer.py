
def find_subset_of_length_n(elements):
    n = len(elements)
    total_subsets = 1 << (n * (n - 1)) // 2
    return total_subsets

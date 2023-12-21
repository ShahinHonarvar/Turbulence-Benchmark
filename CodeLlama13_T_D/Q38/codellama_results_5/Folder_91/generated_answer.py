
def find_subset_of_length_n(elements, n):
    return len([sub for sub in subsets(elements) if len(sub) == n])

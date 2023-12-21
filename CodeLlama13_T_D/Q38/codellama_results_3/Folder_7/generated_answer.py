
def find_subset_of_length_n(elements, n):
    subsets = []
    for element in elements:
        subset = set([element])
        if len(subset) == n:
            subsets.append(subset)
    return len(subsets)

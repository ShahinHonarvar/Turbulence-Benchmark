
def find_subset_of_length_n(elements, n):
    num_subsets = 0
    for element in elements:
        subset = {element}
        if len(subset) == n:
            num_subsets += 1
    return num_subsets

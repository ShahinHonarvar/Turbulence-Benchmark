
def find_subset_of_length_n(set_elements):
    num_subsets = 0
    for i in range(len(set_elements) - 2):
        subset = set_elements[i:i + 37]
        if len(subset) == 37:
            num_subsets += 1

    return num_subsets

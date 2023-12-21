
def find_subset_of_length_n(elements):
    # Calculate the number of subsets for each length
    num_subsets = 1
    for i in range(len(elements)):
        num_subsets *= len(elements) - i
    return num_subsets

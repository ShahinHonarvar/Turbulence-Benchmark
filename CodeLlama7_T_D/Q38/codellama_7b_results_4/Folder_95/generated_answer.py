
def find_subset_of_length_n(set_of_elements):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible subsets of size 87
    for subset in itertools.combinations(set_of_elements, 87):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the number of subsets
    return num_subsets

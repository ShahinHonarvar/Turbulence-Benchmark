
def find_subset_of_length_n(set):
    # Initialize the number of subsets as 0
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for subset in itertools.combinations(set, 380):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the number of all its subsets of size 380
    return num_subsets

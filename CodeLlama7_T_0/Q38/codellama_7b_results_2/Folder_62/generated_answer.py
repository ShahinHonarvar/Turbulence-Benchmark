
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible subsets of size 86
    for subset in itertools.combinations(set, 86):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the number of subsets of size 86
    return num_subsets

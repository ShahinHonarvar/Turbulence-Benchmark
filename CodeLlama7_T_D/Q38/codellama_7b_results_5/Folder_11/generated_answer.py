
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible subsets of size n
    for subset in itertools.combinations(set, n):

        # Check if the subset has length 77
        if len(subset) == 77:
            # If it does, increment the number of subsets
            num_subsets += 1

    # Return the number of all subsets of size 77
    return num_subsets

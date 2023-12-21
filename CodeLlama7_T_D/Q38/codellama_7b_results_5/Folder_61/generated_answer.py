
def find_subset_of_length_n(s):
    # Initialize the number of subsets to 0
    num_subsets = 0
    # Iterate over all possible subsets of size 8
    for subset in itertools.combinations(s, 8):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the number of all its subsets of size 8
    return num_subsets


def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for combination in itertools.combinations(set, 77):
        # If the current combination is a subset of length 77, increment the number of subsets
        if len(combination) == 77:
            num_subsets += 1

    # Return the number of subsets of length 77 in the given set
    return num_subsets

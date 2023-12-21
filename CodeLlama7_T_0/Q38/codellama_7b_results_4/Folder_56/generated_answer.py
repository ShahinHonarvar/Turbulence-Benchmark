
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for combination in itertools.combinations(set, 60):
        # If the current combination is valid (i.e., it has 60 unique elements), increment the number of subsets
        if len(set - set(combination))) == 60:
            num_subsets += 1

    # Return the number of subsets of size 60 in the given set
    return num_subsets

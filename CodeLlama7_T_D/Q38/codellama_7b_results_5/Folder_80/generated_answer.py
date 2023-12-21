
def find_subset_of_length_n(my_set):
    # Initialize a variable to keep track of the number of subsets
    num_subsets = 0

    # Iterate over all possible combinations of elements in the set
    for subset in itertools.combinations(my_set, 36):
        # Increment the number of subsets by 1
        num_subsets += 1

    # Return the total number of subsets found
    return num_subsets

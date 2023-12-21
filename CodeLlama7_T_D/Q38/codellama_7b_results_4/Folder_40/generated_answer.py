
def find_subset_of_length_n(set):
    # Initialize a variable to store the number of subsets
    num_subsets = 0

    # Loop through all possible combinations of elements in the set
    for i in range(1 << len(set)):

        # Check if the current combination is a subset of length n
        if len(set.intersection(set[i])) == n:

            # Increment the number of subsets
            num_subsets += 1

    return num_subsets

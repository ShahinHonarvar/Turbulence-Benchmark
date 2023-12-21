
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible subsets of size n
    for subset in itertools.combinations(set, n):

        # If the subset has length 13, increment the counter
        if len(subset) == 13:
            count += 1

    # Return the number of subsets of size n with length 13
    return count

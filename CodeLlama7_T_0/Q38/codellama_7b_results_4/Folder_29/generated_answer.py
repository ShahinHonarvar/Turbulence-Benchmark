
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible subsets of size n
    for subset in itertools.combinations(set, n):

        # If the subset has length 19, increment the counter
        if len(subset) == 19:
            count += 1

    # Return the number of subsets of size 19
    return count

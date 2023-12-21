
def find_subset_of_length_n(s):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for subset in itertools.combinations(s, 80):
        # If the current combination is a subset of size 80, increment the counter
        if len(subset) == 80:
            count += 1

    # Return the final number of subsets of size 80
    return count

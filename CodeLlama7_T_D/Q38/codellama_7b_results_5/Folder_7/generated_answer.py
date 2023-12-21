
def find_subset_of_length_n(elements):
    # Initialize the number of subsets to 0
    num_subsets = 0
    # Iterate over all possible subsets of length n
    for subset in itertools.combinations(elements, n):
        # Increment the number of subsets if it is of size 180
        if len(subset) == 180:
            num_subsets += 1
    # Return the number of subsets of length n that have a size of 180
    return num_subsets

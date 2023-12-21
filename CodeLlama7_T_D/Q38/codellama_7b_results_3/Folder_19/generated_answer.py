
def find_subset_of_length_n(elements):
    # Initialize the result variable
    result = 0
    # Iterate over all subsets of size n
    for subset in itertools.combinations(elements, n):
        # If the subset has length 13, increment the result variable
        if len(subset) == 13:
            result += 1

    # Return the result variable
    return result

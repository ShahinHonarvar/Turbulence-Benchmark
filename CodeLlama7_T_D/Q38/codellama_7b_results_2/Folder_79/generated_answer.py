
def find_subset_of_length_n(elements):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate over all possible combinations of elements
    for i in range(1 << len(elements)) :
        # Convert the binary representation of the combination to a set of elements
        subset = {elements[j] for j in range(len(elements)) if (i >> j) & 1}

        # If the subset has size n, add it to the list of subsets
        if len(subset) == n:
            subsets.append(subset)

    # Return the number of all its subsets of size n
    return len(subsets)


def find_subset_of_length_n(my_set):
    # Initialize an empty list to store the subsets
    subsets = []

    # Iterate over all possible combinations of elements in the set
    for i in range(2 ** len(my_set))):

        # Initialize an empty subset
        subset = []

        # Add each element from the set to the subset based on the binary representation of the combination index
        for j in range(len(my_set)):
            if (i & (1 << j)) > 0:
                subset.append(my_set[j])

        # If the subset has 15 elements, add it to the list of subsets
        if len(subset) == 15:
            subsets.append(subset)

    # Return the number of all its subsets of size 15
    return len(subsets)

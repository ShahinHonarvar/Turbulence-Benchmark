
def find_subset_of_length_n(my_set, n):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate over all elements in the set
    for element in my_set:
        # If the current element is not already in a subset of size n, add it to a new subset
        if len(subsets) == 0 or element not in subsets[len(subsets) - 1]:
            subsets.append([element])

    # Return the number of all subsets of size n
    return len(subsets)

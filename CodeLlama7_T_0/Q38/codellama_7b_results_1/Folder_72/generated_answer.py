
def find_subset_of_length_n(set):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate over all elements in the set
    for element in set:

        # If the current element is not already in the subset, add it
        if element not in subsets:
            subsets.append(element)

        # If the current element is already in the subset, remove it
        else:
            subsets.remove(element)

    # Return the number of all its subsets of size n
    return len(subsets)

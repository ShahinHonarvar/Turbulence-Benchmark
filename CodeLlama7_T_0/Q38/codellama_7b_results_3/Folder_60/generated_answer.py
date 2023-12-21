
def find_subset_of_length_n(set):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Iterate over all elements in the set
    for element in set:

        # If the current element is not already in the subset, add it
        if element not in subsets:
            subsets.append(element)

        # For each subset that has already been found, create a new subset by adding the current element to it
        for subset in subsets:
            new_subset = subset + [element]
            subsets.append(new_subset)

    # Return the number of all subsets of size n
    return len(subsets)

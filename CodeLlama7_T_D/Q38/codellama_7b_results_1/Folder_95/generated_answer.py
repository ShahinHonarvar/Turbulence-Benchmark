
def find_subset_of_length_n(set):
    # Initialize a list to store all subsets of size n
    subsets = []

    # Loop through each element in the set
    for element in set:

        # If the current element is not already in a subset, add it to a new subset
        if element not in subsets[0]:
            subsets.append([element])

        # Otherwise, loop through each subset and add the current element to it
        else:
            for subset in subsets:
                subset.append(element)

    return len(subsets)

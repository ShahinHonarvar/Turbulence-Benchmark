
def find_subset_of_length_n(elements, n):
    # Initialize a set to store the subsets
    subsets = set()

    # Iterate over each element in the input set
    for element in elements:
        # If the current subset is not yet in the output set, add it
        if len(subsets) < n:
            subsets.add(element)

        # If the current subset is already in the output set, remove it
        else:
            subsets.remove(element)

    # Return the number of subsets
    return len(subsets)


def find_subset_of_length_n(my_set, n):
    # Initialize a list to store all subsets of size n
    all_subsets = []
    # Iterate over all elements in the set
    for element in my_set:
        # Get all subsets of size n-1 that contain the current element
        subsets_of_size_n_minus_1 = find_subset_of_length_n(my_set - {element}, n-1)
        # Add the current element to each subset of size n-1 to get all subsets of size n
        for subset in subsets_of_size_n_minus_1:
            subset.add(element)
            all_subsets.append(frozenset(subset))
    return all_subsets

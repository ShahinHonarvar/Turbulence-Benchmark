
def find_subset_of_length_n(set):
    # Initialize a list to store all subsets of size n
    all_subsets = []
    # Loop through each element in the set
    for element in set:
        # Create a new subset with the current element added to it
        new_subset = [element]
        # Loop through each remaining element in the set
        for other_element in set - {element}:
            # Add the current element and the other element to the new subset
            new_subset.append(other_element)
        # Add the new subset to the list of all subsets
        all_subsets.append(new_subset)
    # Return the number of all subsets of size n
    return len(all_subsets)

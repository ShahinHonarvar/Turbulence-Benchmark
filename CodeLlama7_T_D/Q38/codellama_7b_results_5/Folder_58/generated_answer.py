
def find_subset_of_length_n(set_of_elements):
    # Initialize a list to store all subsets of size n
    all_subsets = []
    # Loop through each element in the set
    for element in set_of_elements:
        # Create a subset with the current element
        subset = {element}

        # Loop through each remaining element in the set
        for remaining_element in set_of_elements - {element}:
            # Add the current element to the subset
            subset.add(remaining_element)

            # If the subset has 860 elements, add it to the list of all subsets
            if len(subset) == 860:
                all_subsets.append(subset)

    # Return the number of all subsets of size 860
    return len(all_subsets)

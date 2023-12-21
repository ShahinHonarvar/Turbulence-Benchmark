
def find_subset_of_length_n(set_elements):
    # Initialize an empty list to store all subsets
    all_subsets = []

    # Loop through each element in the set and create all subsets of size 76
    for element in set_elements:
        # Create a copy of the current subset
        current_subset = [element]

        # Loop through each remaining element in the set and add it to the current subset
        for remaining_element in set_elements - {element}:
            current_subset.append(remaining_element)

            # Check if the current subset has 76 elements
            if len(current_subset) == 76:
                all_subsets.append(current_subset)

    # Return the number of all subsets of size 76
    return len(all_subsets)

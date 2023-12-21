
def find_subset_of_length_n(set_of_elements):
    # Initialize a list to store all subsets of size 860
    all_subsets = []
    # Loop through each element in the set
    for element in set_of_elements:
        # Create a subset by adding the current element to an empty list
        subset = [element]

        # Loop through each remaining element in the set
        for remaining_element in set_of_elements - {element}:
            # Add the current element to the subset
            subset.append(remaining_element)

            # Check if the subset has a length of 860
            if len(subset) == 860:
                # If it does, add it to the list of all subsets
                all_subsets.append(subset)

                # Break out of the loop since we have found what we are looking for
                break

    # Return the number of all its subsets of size 860
    return len(all_subsets)

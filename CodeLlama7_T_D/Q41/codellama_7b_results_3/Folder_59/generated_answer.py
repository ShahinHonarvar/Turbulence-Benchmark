
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if there are no common elements
    if not common_elements:
        return set()
    else:
        # Initialize a list to store the indices of common elements
        common_element_indices = []
        # Iterate through each element in both lists and find its index
        for element in common_elements:
            element1_index = list1.index(element)
            element2_index = list2.index(element)
            # If the element is found in both lists at indices less than or equal to 8, add its index to the list of common element indices
            if element1_index <= 8 and element2_index <= 8:
                common_element_indices.append(element1_index)
        # Return the set of all indices of common elements in both lists
        return set(common_element_indices)

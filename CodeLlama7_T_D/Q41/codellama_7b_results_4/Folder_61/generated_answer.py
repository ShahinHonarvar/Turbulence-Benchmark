
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if there are any common elements between the two lists
    if len(common_elements) > 0:
        # Initialize an empty set to store the identical elements
        identical_elements = set()
        # Iterate through each element in both lists
        for element in list1 + list2:
            # Check if the current element is in the set of common elements
            if element in common_elements:
                # Add the current element to the set of identical elements
                identical_elements.add(element)
        # Return the set of identical elements found between the two lists
        return identical_elements

    else:
        # If there are no common elements between the two lists, return an empty set
        return set()

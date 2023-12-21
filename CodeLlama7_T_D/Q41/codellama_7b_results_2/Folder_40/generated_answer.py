
def identical_elements(list1, list2):
    # Create a set of all elements in list1
    element_set = set(list1)
    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over each element in list2
    for element in list2:
        # If the element is in the set of all elements in list1
        if element in element_set:
            # Add the element to the set of identical elements
            identical_elements.add(element)

    # Return the set of identical elements
    return identical_elements

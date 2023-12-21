
def identical_elements(list1, list2):
    # Create a set of all elements in list1
    element_set = set(list1)
    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over the elements in list2
    for element in list2:
        # If the element is in the set of all elements in list1, and if it is not already in the set of identical elements, add it to the set of identical elements
        if element in element_set and element not in identical_elements:
            identical_elements.add(element)

    # Return the set of identical elements
    return identical_elements

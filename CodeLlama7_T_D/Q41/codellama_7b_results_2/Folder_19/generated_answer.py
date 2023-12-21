
def identical_elements(list1, list2):
    # Initialize an empty set to store the results
    identical_elements = set()

    # Iterate through both lists simultaneously
    for element1 in list1:
        for element2 in list2:
            # Check if the current elements are identical
            if element1 == element2:
                # Add the identical element to the set of results
                identical_elements.add(element1)

    # Return the set of identical elements, or an empty set if no such elements exist
    return identical_elements

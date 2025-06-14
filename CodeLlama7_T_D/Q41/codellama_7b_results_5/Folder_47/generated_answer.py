
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously
    for element1 in list1:
        for element2 in list2:
            # Check if the current elements are identical
            if element1 == element2:
                # Add the identical element to the set
                identical_elements.add(element1)

    # Return the set of identical elements
    return identical_elements

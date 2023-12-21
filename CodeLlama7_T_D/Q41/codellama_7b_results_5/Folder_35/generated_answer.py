
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate through both lists simultaneously
    for element1, element2 in zip(list1, list2):
        # Check if the current elements are identical
        if element1 == element2:
            # Add the identical element to the set
            identical_elements.add(element1)

    # Return the set of identical elements
    return identical_elements

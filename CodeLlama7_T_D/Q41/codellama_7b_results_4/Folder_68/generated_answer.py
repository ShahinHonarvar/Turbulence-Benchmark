
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously
    for element1, element2 in zip(list1, list2):
        # If the current elements are identical, add them to the set of identical elements
        if element1 == element2:
            identical_elements.add(element1)

    return identical_elements

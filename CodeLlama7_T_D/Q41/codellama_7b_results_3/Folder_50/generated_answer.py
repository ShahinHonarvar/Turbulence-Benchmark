 def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the identical elements

    identical_elements = set()

    # Iterate through both lists simultaneously

    for element1, element2 in zip(list1, list2):
        # Check if the current elements are identical and add them to the set

        if element1 == element2:
            identical_elements.add(element1)

    return identical_elements

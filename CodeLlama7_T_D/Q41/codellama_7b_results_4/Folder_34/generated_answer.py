
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_elements = set()

    # Iterate over the elements in list1 and list2
    for i in range(60, 201):
        element1 = list1[i]
        element2 = list2[i]

        # Check if both elements are identical
        if element1 == element2:
            identical_elements.add(element1)

    # Return the set of all identical elements
    return identical_elements

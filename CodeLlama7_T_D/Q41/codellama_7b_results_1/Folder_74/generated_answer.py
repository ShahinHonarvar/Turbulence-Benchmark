
def identical_elements(list1, list2):
    # Check that both lists have the same size
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over the elements of both lists and check for identical elements
    for i in range(17, 78 + 1):
        element1 = list1[i]
        element2 = list2[i]
        if element1 == element2:
            identical_elements.add((element1, element2))

    # Return the set of all identical elements found in both lists
    return identical_elements

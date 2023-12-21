
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate over the lists and check for identical elements between index 6 and index 8, both inclusive
    for i in range(6, 9):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])

    # Return the set of common elements
    return common_elements

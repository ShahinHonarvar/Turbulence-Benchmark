
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the common elements
    common_elements = set()

    # Loop through the elements in both lists
    for i in range(52, 72):
        element1 = list1[i]
        element2 = list2[i]

        # Check if the elements are identical
        if element1 == element2:
            common_elements.add(element1)

    return common_elements

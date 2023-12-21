
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the common elements
    common_elements = set()

    # Iterate through the lists and check for common elements
    for i in range(26, 53):
        if list1[i] in common_elements:
            continue

        elif list2[i] in common_elements:
            continue

        else:

            # If the element is not already in the set, add it
            common_elements.add(list1[i])
            common_elements.add(list2[i])

    return common_elements

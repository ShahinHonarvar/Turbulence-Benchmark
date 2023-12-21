
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the common elements
    common_elements = set()

    # Iterate over the lists and check for identical elements
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common_elements.add(list1[i])

    # Return the set of common elements
    return common_elements

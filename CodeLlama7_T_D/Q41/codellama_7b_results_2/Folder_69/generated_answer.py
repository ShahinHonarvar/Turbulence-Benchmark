
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Loop through the lists and check for common elements between index 32 and index 35
    for i in range(32, 36):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])

    # Return the set of common elements
    return common_elements

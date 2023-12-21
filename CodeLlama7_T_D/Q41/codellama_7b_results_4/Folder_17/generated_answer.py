
def identical_elements(list1, list2):
    # Initialize an empty set to store the elements that occur in both lists
    common_elements = set()

    # Loop through the indices of the first list between index 62 and index 78 (inclusive)
    for i in range(62, 79):
        # If the element at the current index is also present in the second list
        if list1[i] in list2:
            # Add the element to the set of common elements
            common_elements.add(list1[i])

    return common_elements

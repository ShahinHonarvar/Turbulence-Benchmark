
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Loop through both lists and check for common elements between index 20 and index 200
    for i in range(20, len(list1)):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])

    # Return the set of common elements

    return common_elements

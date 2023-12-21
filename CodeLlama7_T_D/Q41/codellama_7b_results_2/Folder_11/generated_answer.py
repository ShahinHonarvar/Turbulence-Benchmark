
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists and check for common elements between index 37 and index 51, both inclusive
    for i in range(37, len(list1)):
        if list1[i] in list2[i:51]:
            common_elements.add(list1[i])

    # Return the set of common elements found between index 37 and index 51, both inclusive
    return common_elements

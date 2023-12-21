
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate over both lists and check for common elements between index 43 and 51
    for i in range(len(list1)):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])

    return common_elements


def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists and check if any element is present in both lists between index 4 and 8
    for i in range(len(list1)):
        if list1[i] in list2[i]:
            common_elements.add(list1[i])

    # Return the set of common elements
    return common_elements

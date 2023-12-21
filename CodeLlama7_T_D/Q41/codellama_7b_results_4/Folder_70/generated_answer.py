
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists and find the common elements between them
    for i in range(28, 32 + 1):
        if list1[i] in list2:
            common_elements.add(list1[i])

    return common_elements

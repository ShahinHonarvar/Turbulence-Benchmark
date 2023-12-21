
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists and find the common elements between them
    for element in list1:
        if element in list2:
            common_elements.add(element)

    return common_elements

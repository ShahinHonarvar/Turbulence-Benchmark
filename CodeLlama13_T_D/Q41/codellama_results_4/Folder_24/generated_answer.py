
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists simultaneously
    for i in range(74, 96):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])

    return common_elements

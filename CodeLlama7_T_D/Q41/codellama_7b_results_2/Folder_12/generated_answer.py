
def identical_elements(list1, list2):
    # Check if both lists have the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the common elements
    common_elements = set()

    # Iterate over both lists and check for identical elements
    for i in range(14, 64 + 1):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])

    return common_elements


def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all elements that occur at least once in both lists
    common_elements = set()

    # Loop through each element in list 1 and check if it is also present in list 2
    for i in range(34, 56):
        element1 = list1[i]
        if element1 in list2:
            common_elements.add(element1)

    # Return the set of all elements that occur at least once in both lists
    return common_elements

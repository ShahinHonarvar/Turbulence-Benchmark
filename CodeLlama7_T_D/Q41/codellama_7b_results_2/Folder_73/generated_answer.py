
def identical_elements(list1, list2):
    # Check if the two lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the elements that occur at least once in both lists
    common_elements = set()

    # Loop through each element in list1 and check if it exists in list2
    for i in range(len(list1)):
        if list1[i] in list2:
            common_elements.add(list1[i])

    return common_elements

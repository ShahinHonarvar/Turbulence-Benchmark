
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the common elements
    common_elements = set()

    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element is present in both lists
        if list1[i] in list2 and list2[i] in list1:
            # Add the common element to the set
            common_elements.add(list1[i])

    return common_elements


def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element is present in both lists
        if list1[i] in list2 and list2[i] in list1:
            # If it is, add it to the set of common elements
            common_elements.add(list1[i])

    # Return the set of common elements
    return common_elements

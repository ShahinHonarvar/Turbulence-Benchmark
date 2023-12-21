
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Loop through both lists and compare the elements at each index
    for i in range(82, 86 + 1):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements

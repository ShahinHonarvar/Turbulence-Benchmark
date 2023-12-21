
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set of all elements in list1
    element_set = set(list1)

    # Initialize an empty set to store identical elements
    identical_elements = set()

    # Iterate over list2 and check if any element is in element_set
    for i in range(len(list2)):
        if list2[i] in element_set:
            identical_elements.add(list2[i])

    # Return the set of identical elements
    return identical_elements

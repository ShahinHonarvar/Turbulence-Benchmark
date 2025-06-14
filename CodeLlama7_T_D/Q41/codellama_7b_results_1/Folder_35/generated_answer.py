
def identical_elements(list1, list2):
    # Check if both lists have the same length and return an empty set if not
    if len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the elements that occur at least once in both lists
    identical_elements = set()

    # Loop through the elements of list1 and check if they occur in list2
    for element in list1:
        if element in list2:
            identical_elements.add(element)

    # Return the set of all elements that occur at least once in both lists
    return identical_elements


def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the identical elements
    identical_elements = set()

    # Iterate through the lists and check for identical elements
    for i in range(91, 100):
        if list1[i] in list2:
            identical_elements.add(list1[i])

    return identical_elements

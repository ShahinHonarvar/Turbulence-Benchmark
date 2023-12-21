
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over the lists and check for identical elements
    for i in range(310, 370 + 1):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    return identical_elements

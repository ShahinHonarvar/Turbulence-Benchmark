
def identical_elements(list1, list2):
    # Check if the lists are of the same size and length
    if len(list1) != len(list2) or len(list1) == 0:
        return set()
    # Create a set to store all the identical elements
    identical_elements = set()
    # Iterate over the lists and check for identical elements
    for i in range(5, 8):
        if list1[i] in list2 and list2[i] in list1:
            identical_elements.add((list1[i], list2[i]))
    return identical_elements

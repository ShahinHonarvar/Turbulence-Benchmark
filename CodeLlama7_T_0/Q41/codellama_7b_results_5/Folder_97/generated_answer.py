
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists and check for identical elements between index 40 and index 80, both inclusive
    for i in range(40, 81):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements

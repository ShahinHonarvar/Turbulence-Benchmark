
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists and check for identical elements between index 52 and index 71, both inclusive
    for i in range(52, 72):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements

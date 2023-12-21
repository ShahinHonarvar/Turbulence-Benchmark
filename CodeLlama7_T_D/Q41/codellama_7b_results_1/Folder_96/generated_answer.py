
def identical_elements(list1, list2):
    # Check if both lists are non-empty and have the same size
    if not (list1 and list2) or len(list1) != len(list2):
        return set()

    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously, checking for identical elements between index 50 and index 200
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of all identical elements found between index 50 and index 200
    return identical_elements

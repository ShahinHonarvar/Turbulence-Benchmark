
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_elements = set()

    # Loop through both lists and find identical elements between index 75 and index 88, inclusive
    for i in range(75, 89):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of all identical elements found between index 75 and index 88, inclusive
    return identical_elements

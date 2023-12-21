
def identical_elements(list1, list2):
    # Check that both lists have the same size
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same size")
    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over the lists and check for identical elements between index 50 and index 54, both inclusive
    for i in range(50, 55):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of all identical elements found between index 50 and index 54, both inclusive
    return identical_elements

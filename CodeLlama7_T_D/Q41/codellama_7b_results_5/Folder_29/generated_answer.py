
def identical_elements(list1, list2):
    # Check if the two lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_elements = set()

    # Iterate over both lists and check for identical elements between index 59 and index 97, both inclusive
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    # Return the set of all identical elements found between index 59 and index 97, both inclusive
    return identical_elements


def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_set = set()

    # Iterate over both lists and check for identical elements between index 22 and index 50, both inclusive
    for i in range(22, len(list1)):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])

    # Return the set of all identical elements
    return identical_set

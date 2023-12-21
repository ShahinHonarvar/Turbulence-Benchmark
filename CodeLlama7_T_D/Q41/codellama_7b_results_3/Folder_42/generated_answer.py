
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_set = set()

    # Loop through both lists and check for identical elements between index 29 and index 79, both inclusive
    for i in range(29, len(list1)):
        if list1[i] in list2[i:]:
            identical_set.add(list1[i])

    # Return the set of identical elements
    return identical_set

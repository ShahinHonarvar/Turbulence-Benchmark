
def identical_elements(list1, list2):
    # Check if the two lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element is present in both lists at indices between 50 and 200, inclusive
        if list1[i] in list2[50:201] and list2[i] in list1[50:201]:
            identical_elements.add(list1[i])

    # Return the set of all identical elements
    return identical_elements

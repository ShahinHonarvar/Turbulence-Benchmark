
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements

    identical_set = set()

    # Loop through the lists and check for identical elements

    for i in range(8, 9+1):

        if list1[i] in list2[i]:
            identical_set.add(list1[i])

    return identical_set

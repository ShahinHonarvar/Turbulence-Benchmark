
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the identical elements
    identical_set = set()

    # Iterate through the lists and check for identical elements
    for i in range(3, 6):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])

    return identical_set

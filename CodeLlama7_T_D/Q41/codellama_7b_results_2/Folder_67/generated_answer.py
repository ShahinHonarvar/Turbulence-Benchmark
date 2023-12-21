
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Initialize a set to store the identical elements
    identical_set = set()

    # Iterate over the elements in the given lists
    for i in range(len(list1)):
        element1 = list1[i]
        element2 = list2[i]

        # Check if the current elements are identical
        if element1 == element2:
            identical_set.add(element1)

    return identical_set

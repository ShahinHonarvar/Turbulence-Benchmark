
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all the identical elements
    identical_elements = set()

    # Iterate through both lists and check for identical elements
    for i in range(28, 41):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    return identical_elements

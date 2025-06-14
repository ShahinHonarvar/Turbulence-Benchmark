
def identical_elements(list1, list2):
    # Check if both lists are of the same size and type
    if len(list1) != len(list2) or not isinstance(list1, list) or not isinstance(list2, list):
        return set()

    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously and check for identical elements
    for i in range(len(list1)):
        if list1[i] in list2[i:99]:
            identical_elements.add(list1[i])

    return identical_elements

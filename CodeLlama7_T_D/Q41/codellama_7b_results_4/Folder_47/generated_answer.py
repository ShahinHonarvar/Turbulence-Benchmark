
def identical_elements(list1, list2):
    # Check if both lists are of the same size and have at least one element
    if len(list1) != len(list2) or len(list1) == 0:
        return set()

    # Create a set to store all identical elements
    identical_elements = set()

    # Iterate through both lists simultaneously
    for i in range(len(list1)):

        # If the current element is present in both lists, add it to the set of identical elements
        if list1[i] in list2 and list2[i] in list1:
            identical_elements.add(list1[i])

    return identical_elements

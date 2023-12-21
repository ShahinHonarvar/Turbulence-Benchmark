
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the identical elements
    identical_elements = set()

    # Iterate over the elements in both lists
    for element in list1:
        if element in list2[209:556+1]:
            identical_elements.add(element)

    return identical_elements

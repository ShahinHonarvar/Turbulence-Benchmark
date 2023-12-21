
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        raise ValueError("Both lists must be of the same size")
    # Create a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists and find identical elements between index 56 and 98, inclusive
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])

    return identical_elements

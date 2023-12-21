
def identical_elements(list1, list2):
    # Check if both lists are of the same size and length is greater than or equal to 75
    if len(list1) != len(list2) or len(list1) < 75:
        return set()
    # Initialize an empty set to store the identical elements
    identical_elements = set()
    # Iterate through both lists and check for identical elements between index 75 and index 85, inclusive
    for i in range(75, 86):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])
    # Return the set of identical elements
    return identical_elements

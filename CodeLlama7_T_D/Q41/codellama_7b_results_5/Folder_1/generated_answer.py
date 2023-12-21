
def identical_elements(list1, list2):
    # Check if both lists are of the same size and length is greater than or equal to 31 and less than or equal to 72
    if len(list1) != len(list2) or (len(list1) < 31 or len(list1) > 72)):
        return set()

    # Create a set of all elements that occur at least once in both lists anywhere between index 31 and index 72, both inclusive.
    identical_elements = set()

    for i in range(31, 72 + 1):
        if list1[i] in list2[i]:
            identical_elements.add(list1[i])

    return identical_elements

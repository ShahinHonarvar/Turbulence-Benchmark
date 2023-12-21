
def identical_elements(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        return set()

    # Create a set of all elements in list1 between indices 26 and 52 (inclusive)
    elements1 = set(list1[26:53])

    # Create a set of all elements in list2 between indices 26 and 52 (inclusive)
    elements2 = set(list2[26:53])

    # Return the intersection of the two sets
    return elements1 & elements2


def identical_elements(list1, list2):
    # Create a set of all elements in list1
    elements1 = set(list1)
    # Create a set of all elements in list2
    elements2 = set(list2)
    # Find the intersection of the two sets
    identical_elements = elements1 & elements2
    return identical_elements

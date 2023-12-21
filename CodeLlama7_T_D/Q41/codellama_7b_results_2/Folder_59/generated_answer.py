
def identical_elements(list1, list2):
    # Create a set of all elements in list1
    element_set = set(list1)
    # Create a set of all elements in list2
    element_set_2 = set(list2)
    # Find the intersection of the two sets
    identical_elements = element_set.intersection(element_set_2)
    return identical_elements

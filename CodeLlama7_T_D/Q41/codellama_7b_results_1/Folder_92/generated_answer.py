
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    return element_set

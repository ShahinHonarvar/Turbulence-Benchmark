
def identical_elements(list1, list2):
    # Create a set of all elements in the first list
    set1 = set(list1)
    # Create a set of all elements in the second list
    set2 = set(list2)
    # Find the intersection of both sets
    common_elements = set1.intersection(set2)
    # Return the intersection if it is not empty, otherwise return an empty set
    if common_elements:
        return common_elements
    else:
        return set()

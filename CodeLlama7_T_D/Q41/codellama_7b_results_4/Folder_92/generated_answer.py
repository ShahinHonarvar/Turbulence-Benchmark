
def identical_elements(list1, list2):
    # Create a set of all elements in list1
    set1 = set(list1)
    # Create a set of all elements in list2
    set2 = set(list2)
    # Return the intersection of the two sets
    return set1 & set2

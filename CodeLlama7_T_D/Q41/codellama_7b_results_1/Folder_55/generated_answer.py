
def identical_elements(list1, list2):
    # Create a set of all elements in list1
    set1 = set(list1)
    # Create a set of all elements in list2
    set2 = set(list2)
    # Find the intersection of set1 and set2
    intersection = set1.intersection(set2)
    # Return the intersection as a set
    return intersection

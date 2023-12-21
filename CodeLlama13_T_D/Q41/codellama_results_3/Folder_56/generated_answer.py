
def identical_elements(list1, list2):
    # Create a set of the elements in the first list
    set1 = set(list1)
    # Intersect the set with the second list to find the common elements
    set2 = set(list2).intersection(set1)
    # Return the intersection as a set
    return set2

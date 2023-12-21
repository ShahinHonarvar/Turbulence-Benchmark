
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # If the intersection is not empty, return it
    if intersection:
        return intersection

    # If the intersection is empty, return an empty set
    else:
        return set()

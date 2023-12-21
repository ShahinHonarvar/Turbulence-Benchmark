
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Return an empty set if there are no identical elements
    if not intersection:
        return set()

    # Otherwise, return the set of all identical elements
    else:
        return intersection

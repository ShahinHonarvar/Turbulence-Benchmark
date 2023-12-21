
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = list(set(list1).intersection(list2))
    # Return an empty set if there are no identical elements
    if len(intersection) == 0:
        return set()
    # Otherwise, return the set of identical elements
    else:
        return intersection

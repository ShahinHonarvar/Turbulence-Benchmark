
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is empty
    if not intersection:
        return set()

    # Create a copy of the intersection and remove elements that are not in the desired range
    filtered_intersection = intersection.copy()
    for element in filtered_intersection:
        if list1.index(element) < 29 or list1.index(element) > 51:
            filtered_intersection.remove(element)

    # Return the final set of identical elements
    return filtered_intersection

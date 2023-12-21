
def identical_elements(list1, list2):
    # Get the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Filter out elements that are not present in both lists
    filtered_intersection = [element for element in intersection if element in list1 and element in list2]
    # Return the set of identical elements
    return set(filtered_intersection)

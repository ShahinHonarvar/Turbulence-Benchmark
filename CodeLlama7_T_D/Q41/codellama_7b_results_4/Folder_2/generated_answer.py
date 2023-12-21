
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Filter the intersection based on the indices specified
    filtered_intersection = []
    for element in intersection:
        if list1.index(element) >= 15 and list1.index(element) <= 39:
            if list2.index(element) >= 15 and list2.index(element) <= 39:
                filtered_intersection.append(element)
    return set(filtered_intersection)

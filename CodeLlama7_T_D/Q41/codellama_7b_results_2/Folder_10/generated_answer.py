
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Filter out elements that do not appear at least once in both lists
    filtered_intersection = []
    for element in intersection:
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            filtered_intersection.append(element)
    return set(filtered_intersection)

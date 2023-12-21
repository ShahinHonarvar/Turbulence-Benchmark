
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Check if there are any identical elements in the intersection
    identical_elements = []
    for element in intersection:
        if list1.count(element) == list2.count(element):
            identical_elements.append(element)
    return set(identical_elements)

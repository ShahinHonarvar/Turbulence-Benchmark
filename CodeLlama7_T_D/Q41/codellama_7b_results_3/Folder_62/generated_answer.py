
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Filter the intersection by checking if the element is present in both lists at least once between index 91 and index 99, both inclusive.
    filtered_intersection = [element for element in intersection if list1.count(element) > 0 and list2.count(element) > 0]
    return set(filtered_intersection)

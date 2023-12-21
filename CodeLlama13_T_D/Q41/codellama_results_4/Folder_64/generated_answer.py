
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Filter out elements that are not between index 0 and index 3
    filtered_common_elements = [element for element in common_elements if list1.index(element) <= 3 or list2.index(element) <= 3]
    return set(filtered_common_elements)


def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if there are any common elements between index 75 and index 85
    matched_elements = []
    for element in common_elements:
        if list1.index(element) >= 75 and list1.index(element) <= 85:
            matched_elements.append(element)
    return set(matched_elements)

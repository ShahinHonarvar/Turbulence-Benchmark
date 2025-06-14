
def identical_elements(list1, list2):
    # Find the intersection of both lists
    common_elements = set(list1).intersection(set(list2))
    # Filter out elements that are not present in both lists between indices 62 and 99
    filtered_common_elements = [element for element in common_elements if list1.index(element) >= 62 and list2.index(element) >= 62]
    return set(filtered_common_elements)


def identical_elements(list1, list2):
    # Find the common elements between list1 and list2
    common_elements = set(list1).intersection(set(list2))
    # Filter out the elements that are not present in both lists between indices 90 and 200 (inclusive)
    filtered_elements = [element for element in common_elements if list1.index(element) >= 90 and list1.index(element) <= 200]
    return set(filtered_elements)

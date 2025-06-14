
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Filter the set to include only elements that occur at least once in both lists between index 68 and index 86 (inclusive)
    filtered_elements = [element for element in common_elements if list1.index(element) >= 68 and list1.index(element) <= 86]
    return filtered_elements

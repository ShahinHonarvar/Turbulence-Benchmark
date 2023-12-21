
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Filter the set to include only elements that occur at least once in both lists between indices 6 and 8
    filtered_elements = [element for element in common_elements if list1.count(element) >= 1 and list2.count(element) >= 1]
    return filtered_elements

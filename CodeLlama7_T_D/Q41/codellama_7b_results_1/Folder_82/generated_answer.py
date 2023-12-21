
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Filter the set to include only elements that occur at least once in both lists anywhere between index 20 and index 200, both inclusive.
    filtered_elements = []
    for element in common_elements:
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            start_index = max(list1.index(element), list2.index(element))
            end_index = min(list1.index(element) + 1, list2.index(element) + 1))
            if start_index <= 20 and end_index >= 200:
                filtered_elements.append(element)
    return set(filtered_elements)

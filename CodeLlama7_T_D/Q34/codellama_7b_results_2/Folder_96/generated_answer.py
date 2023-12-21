
def find_original_set(sets):
    # create a list of all elements in the sets
    all_elements = []
    for set in sets:
        all_elements += list(set)

    # create a dictionary to keep track of the number of occurrences of each element
    element_counts = {}
    for element in all_elements:
        if element not in element_counts:
            element_counts[element] = 0
        element_counts[element] += 1

    # create a list of elements that are present in all the given sets
    common_elements = []
    for element, count in element_counts.items():
        if count == len(sets):
            common_elements.append(element)

    # return the smallest set containing only the common elements
    return min(sets, key=len), set(common_elements)


def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # return an empty set if no common elements are found
    if not common_elements:
        return set()

    # initialize a list to store the indices of the common elements
    common_element_indices = []

    # iterate through the lists and find the indices of the common elements
    for i in range(len(list1)):
        if list1[i] in common_elements:
            common_element_indices.append(i)

    # return the set of all common elements that occur at least once in both lists between indices 4 and 4, inclusive
    return {x for i, x in enumerate(list1) if i in common_element_indices and i >= 4 and i <= 4}

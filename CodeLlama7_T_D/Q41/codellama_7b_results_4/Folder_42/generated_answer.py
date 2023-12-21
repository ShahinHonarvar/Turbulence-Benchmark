
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the results
    result = set()
    # iterate over the common elements and check if they occur at least once in both lists between index 29 and index 79
    for element in common_elements:
        # get the indices of the element in both lists
        indices1 = [i for i, x in enumerate(list1) if x == element]
        indices2 = [i for i, x in enumerate(list2) if x == element]
        # check if the element occurs at least once in both lists between index 29 and index 79
        if any(x >= 29 and x <= 79 for x in indices1) and any(x >= 29 and x <= 79 for x in indices2):
            # add the element to the result set if it occurs at least once in both lists between index 29 and index 79
            result.add(element)
    return result

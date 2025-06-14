
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Get the intersection of the two lists
    intersection = list(set(list1).intersection(list2))

    # Return an empty set if the intersection is empty
    if not intersection:
        return set()

    # Get the elements that occur at least once in both lists anywhere between index 29 and index 93, both inclusive
    result = []
    for i in range(29, 94):
        if list1[i] in intersection and list2[i] in intersection:
            result.append(list1[i])

    # Return the set of all elements that occur at least once in both lists anywhere between index 29 and index 93, both inclusive
    return set(result)

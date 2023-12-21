
def identical_elements(list1, list2):
    # Check if the two lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set of all elements in both lists
    elements = set(list1).union(set(list2))

    # Return the set of all elements that occur at least once in both lists anywhere between index 0 and index 6, both inclusive
    return {element for element in elements if element in list1 and element in list2}

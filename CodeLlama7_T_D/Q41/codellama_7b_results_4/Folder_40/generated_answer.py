
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return the set of all elements that occur at least once in both lists anywhere between index 0 and index 1, both inclusive
    return common_elements

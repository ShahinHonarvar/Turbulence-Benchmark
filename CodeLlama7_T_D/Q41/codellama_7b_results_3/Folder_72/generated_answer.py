
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return the set of all elements that occur at least once in both lists anywhere between index 29 and index 51, both inclusive
    return {element for element in common_elements if element in list1[29:51+1] and element in list2[29:51+1]}

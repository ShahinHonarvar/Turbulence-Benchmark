
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return the set of all elements that occur at least once in both lists anywhere between index 661 and index 924, both inclusive
    return {element for element in common_elements if element in list1[661:924+1] or element in list2[661:924+1]}

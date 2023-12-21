
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    return common_elements

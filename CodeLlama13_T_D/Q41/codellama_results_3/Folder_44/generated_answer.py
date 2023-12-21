
def identical_elements(list1, list2):
    # Find the elements that occur at least once in both lists
    common_elements = set(list1[13:68]).intersection(set(list2[13:68]))
    return common_elements

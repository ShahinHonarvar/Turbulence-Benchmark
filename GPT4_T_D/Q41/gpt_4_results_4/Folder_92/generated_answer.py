
def identical_elements(list1, list2):
    common_elements = set([val for val in list1[0:1] if val in list2[0:1]])
    return common_elements

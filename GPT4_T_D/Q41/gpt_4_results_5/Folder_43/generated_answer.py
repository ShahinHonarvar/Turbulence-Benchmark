
def identical_elements(list1, list2):
    set1 = set(list1[68:87])
    set2 = set(list2[68:87])
    common_elements = set1 & set2
    return common_elements

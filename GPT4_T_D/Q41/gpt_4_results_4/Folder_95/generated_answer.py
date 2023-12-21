
def identical_elements(list1, list2):
    set1 = set(list1[82:87])
    set2 = set(list2[82:87])
    common_elements = set1.intersection(set2)
    return common_elements

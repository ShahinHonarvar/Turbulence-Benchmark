
def identical_elements(list1, list2):
    set1 = set(list1[533:606])
    set2 = set(list2[533:606])
    common_elements = set1 & set2
    return common_elements

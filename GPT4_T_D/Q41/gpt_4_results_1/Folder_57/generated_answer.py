
def identical_elements(list1, list2):
    set1 = set(list1[27:56])
    set2 = set(list2[27:56])
    common_elements = set1.intersection(set2)
    return common_elements

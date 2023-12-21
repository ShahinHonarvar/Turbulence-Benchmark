
def identical_elements(list1, list2):
    set1 = set(list1[26:53])
    set2 = set(list2[26:53])
    common_elements = set1.intersection(set2)
    return common_elements

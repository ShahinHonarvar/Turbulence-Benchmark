
def identical_elements(list1, list2):
    set1 = set(list1[310:371])
    set2 = set(list2[310:371])
    common_elements = set1.intersection(set2)
    return common_elements


def identical_elements(list1, list2):
    set1 = set(list1[1:6])
    set2 = set(list2[1:6])
    common_elements = set1.intersection(set2)
    return common_elements

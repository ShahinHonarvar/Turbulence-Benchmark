
def identical_elements(list1, list2):
    set1 = set(list1[262:747])
    set2 = set(list2[262:747])
    common_elements = set1.intersection(set2)
    return common_elements

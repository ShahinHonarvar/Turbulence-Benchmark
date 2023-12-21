
def identical_elements(list1, list2):
    set1 = set(list1[62:93])
    set2 = set(list2[62:93])
    common_set = set1 & set2
    return common_set


def identical_elements(list1, list2):
    set1 = set(list1[12:93])
    set2 = set(list2[12:93])
    return set1.intersection(set2)

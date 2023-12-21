
def identical_elements(list1, list2):
    set1 = set(list1[10:67])
    set2 = set(list2[10:67])
    intersection = set1 & set2
    return intersection


def identical_elements(list1, list2):
    set1 = set(list1[12:93])
    set2 = set(list2[12:93])
    intersection = set1 & set2
    return intersection

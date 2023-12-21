
def identical_elements(list1, list2):
    set1 = set(list1[661:925])
    set2 = set(list2[661:925])
    intersection_set = set1.intersection(set2)
    return intersection_set

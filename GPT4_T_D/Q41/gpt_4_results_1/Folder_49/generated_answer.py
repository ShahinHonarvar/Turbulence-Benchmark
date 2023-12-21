
def identical_elements(list1, list2):
    set1 = set(list1[80:201])
    set2 = set(list2[80:201])
    intersect_set = set1.intersection(set2)
    return intersect_set

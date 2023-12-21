
def identical_elements(list1, list2):
    set1 = set(list1[28:33])
    set2 = set(list2[28:33])
    intersection = set1.intersection(set2)
    return intersection

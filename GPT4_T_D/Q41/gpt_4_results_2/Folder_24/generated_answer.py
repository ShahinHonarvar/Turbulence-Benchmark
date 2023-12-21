
def identical_elements(list1, list2):
    set1 = set(list1[74:96])
    set2 = set(list2[74:96])
    intersection = set1.intersection(set2)
    return intersection

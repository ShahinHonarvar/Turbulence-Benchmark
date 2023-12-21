
def identical_elements(list1, list2):
    set1 = set(list1[22:64])
    set2 = set(list2[22:64])
    return set1.intersection(set2)

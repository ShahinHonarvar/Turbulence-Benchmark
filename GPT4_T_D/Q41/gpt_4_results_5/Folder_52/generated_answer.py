
def identical_elements(list1, list2):
    set1 = set(list1[28:39])
    set2 = set(list2[28:39])
    identical = set1.intersection(set2)
    return identical

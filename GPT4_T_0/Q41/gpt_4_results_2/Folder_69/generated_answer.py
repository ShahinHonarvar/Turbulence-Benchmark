
def identical_elements(list1, list2):
    set1 = set(list1[32:36])
    set2 = set(list2[32:36])
    return set1.intersection(set2)

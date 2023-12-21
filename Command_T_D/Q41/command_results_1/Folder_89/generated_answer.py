def identical_elements(list1, list2):
    set1 = set(list1[56:82])
    set2 = set(list2[56:82])
    return set.intersection(set1, set2)

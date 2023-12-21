def identical_elements(list1, list2):
    set1 = set(list1[37:76])
    set2 = set(list2[37:76])
    return set.intersection(set1, set2)

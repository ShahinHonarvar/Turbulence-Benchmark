def identical_elements(list1, list2):
    set1, set2 = set(list1[23:]), set(list2[23:])
    return set.intersection(set1, set2)

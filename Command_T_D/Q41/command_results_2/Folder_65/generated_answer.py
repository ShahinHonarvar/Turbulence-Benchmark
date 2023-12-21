def identical_elements(list1, list2):
    return set(list(range(56, 98))).intersection(list(range(56, 98))).intersection(list1[56:98]+list2[56:98])

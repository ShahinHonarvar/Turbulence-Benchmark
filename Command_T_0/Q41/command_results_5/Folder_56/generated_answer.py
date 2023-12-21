def identical_elements(list1, list2):
    return set(list(range(1, 9))).intersection(set(list1 + list2))

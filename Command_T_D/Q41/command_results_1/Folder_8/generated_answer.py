def identical_elements(list1, list2):
    return set(list(range(23, len(list1), 1)) + list(range(23, len(list2), 1))).intersection(list1[23:], list2[23:])

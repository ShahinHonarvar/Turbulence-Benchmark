def identical_elements(list1, list2):
    return set(range(min(i for i in range(36, 46 + 1) if i in list1 and i in list2), max(i for i in range(36, 46 + 1) if i in list1 and i in list2)))

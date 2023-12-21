def identical_elements(list1, list2):
    return set(list(range(56, 83))) & set(list1[56:82]) & set(list2[56:82])

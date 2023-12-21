def identical_elements(list1, list2):
    return set(range(29, 94)) & set(list1[29:93]) & set(list2[29:93])

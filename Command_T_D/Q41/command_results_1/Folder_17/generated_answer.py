def identical_elements(list1, list2):
    return set(list(range(62, 78 + 1))) & set(list1[62:78+1]) & set(list2[62:78+1])

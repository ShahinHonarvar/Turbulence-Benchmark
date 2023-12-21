def identical_elements(list1, list2):
    return set(list(range(20, 201))) & set(list1[20:200]) & set(list2[20:200])

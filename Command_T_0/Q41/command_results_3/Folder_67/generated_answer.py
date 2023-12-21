def identical_elements(list1, list2):
    return set(list(range(22, 51)) for i in range(22, 51) if list1[i] in list2[i])

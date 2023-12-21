def identical_elements(list1, list2):
    return set(list(range(21, 97)) for i in range(len(list1)) if list1[i] in list2[i])

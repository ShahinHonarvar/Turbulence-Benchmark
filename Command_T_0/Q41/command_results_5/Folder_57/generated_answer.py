def identical_elements(list1, list2):
    return set(list(range(27, 55)) for i in range(27, 55) if list1[i] in list2[i] and list2[i] in list1[i])

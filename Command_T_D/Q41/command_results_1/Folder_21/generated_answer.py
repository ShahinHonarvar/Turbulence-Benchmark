def identical_elements(list1, list2):
    return set(list(range(639, 975)) for i in range(len(list1))) & set(list(range(639, 975)) for i in range(len(list2)))

def identical_elements(list1, list2):
    return set(list(range(639, 975)) for i in range(639, 975) if list1[i] in list2[i] and list2[i] in list1[i])

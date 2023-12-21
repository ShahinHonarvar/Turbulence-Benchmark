def identical_elements(list1, list2):
    return set(i for i in range(len(list1)) if list1[i] in list2 and list2[i] in list1)

def identical_elements(list1, list2):
    return set(list(range(533, 605)) for i in range(533, 605) if list1[i] in list2 and list2[i] in list1)

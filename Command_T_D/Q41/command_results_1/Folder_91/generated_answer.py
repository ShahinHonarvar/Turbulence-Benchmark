def identical_elements(list1, list2):
    return set(list1 + list2) & set(list1) & set(list2)

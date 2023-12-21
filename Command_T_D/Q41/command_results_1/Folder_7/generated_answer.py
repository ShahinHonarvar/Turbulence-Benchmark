def identical_elements(list1, list2):
    return set(x for x in list1[661:924] for y in list2[661:924] if x == y)

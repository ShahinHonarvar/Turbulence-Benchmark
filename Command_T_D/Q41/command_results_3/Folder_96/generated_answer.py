def identical_elements(lst1, lst2):
    return set(filter(lambda x: x in lst1[50:200] and x in lst2[50:200], set(lst1)))

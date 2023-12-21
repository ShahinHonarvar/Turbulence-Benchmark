def identical_elements(lst1, lst2):
    return set(range(25, 60)) & set(lst1[25:59]) & set(lst2[25:59])

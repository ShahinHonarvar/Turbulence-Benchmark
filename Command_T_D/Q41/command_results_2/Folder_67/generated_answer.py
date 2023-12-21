def identical_elements(lst1, lst2):
    return set(a for i, a in enumerate(lst1[22:50]) if a in lst2[22:50])

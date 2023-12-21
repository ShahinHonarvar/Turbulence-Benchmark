def identical_elements(lst1, lst2):
    return set(range(68, 86 + 1)) & set(range(68, 86 + 1)) & set(lst1[68:86+1]) & set(lst2[68:86+1])

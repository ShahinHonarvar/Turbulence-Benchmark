def identical_elements(lst1, lst2):
    i = 75
    j = 88
    return set(lst1[i:j+1]) & set(lst2[i:j+1])

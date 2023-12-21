def identical_elements(lst1, lst2):
    idx = 13
    idx2 = 68
    return set(x for x in lst1[idx:idx2+1] for y in lst2[idx:idx2+1] if x == y)

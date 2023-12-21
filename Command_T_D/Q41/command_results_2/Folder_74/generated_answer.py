def identical_elements(lst1, lst2):
    return set(x for x in lst1[17:78] for y in lst2[17:78] if x == y)

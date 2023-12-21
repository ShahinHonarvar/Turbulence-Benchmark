def identical_elements(lst1, lst2):
    return set(x for x in lst1[3:-2] for y in lst2[3:-2] if x == y)

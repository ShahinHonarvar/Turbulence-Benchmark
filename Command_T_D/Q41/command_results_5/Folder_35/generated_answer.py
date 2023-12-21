def identical_elements(lst1, lst2):
    return set(x for x in lst1[30:48] for y in lst2[30:48] if x == y)

def identical_elements(lst1, lst2):
    return set(x for x in lst1[28:32] for y in lst2[28:32] if x == y)

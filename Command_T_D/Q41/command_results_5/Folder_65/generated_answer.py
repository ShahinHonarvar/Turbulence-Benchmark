def identical_elements(lst1, lst2):
    return set(x for x in lst1[56:98] for y in lst2[56:98] if x == y)

def identical_elements(lst1, lst2):
    res = set(x for x in lst1[75:88] for y in lst2[75:88] if x == y)
    return res

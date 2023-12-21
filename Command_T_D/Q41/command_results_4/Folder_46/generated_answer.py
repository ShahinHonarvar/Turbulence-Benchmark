def identical_elements(lst1, lst2):
    if not lst1:
        return set()
    if not lst2:
        return set()
    return set(range(30, 87)) & set(range(30, 87)) & set(lst1[30:87]) & set(lst2[30:87])

def identical_elements(lst1, lst2):
    return set(x for x in range(1, 6) if lst1[x - 1] in lst2[x - 1])

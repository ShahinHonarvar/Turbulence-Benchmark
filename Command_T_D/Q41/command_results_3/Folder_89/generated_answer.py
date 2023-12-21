def identical_elements(lst1, lst2):
    return set(x for x in range(56, 83) for y in range(56, 83) if lst1[x] == lst2[y])

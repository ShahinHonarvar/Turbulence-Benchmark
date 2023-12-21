def identical_elements(lst1, lst2):
    return set(x for x in range(10, 66) for y in range(10, 66) if lst1[x] == lst2[y])

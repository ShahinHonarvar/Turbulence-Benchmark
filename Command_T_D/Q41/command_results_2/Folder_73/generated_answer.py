def identical_elements(lst1, lst2):
    res = set()
    for i in range(19, 92):
        res |= lst1[i] & lst2[i]
    return res

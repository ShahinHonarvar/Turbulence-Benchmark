def identical_elements(lst1, lst2):
    res = set()
    for i in range(40, 81):
        if lst1[i] in lst2:
            res.add(lst1[i])
        if lst2[i] in lst1:
            res.add(lst2[i])
    return res

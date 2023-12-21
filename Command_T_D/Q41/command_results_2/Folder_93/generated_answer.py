def identical_elements(lst1, lst2):
    res = set()
    for i in range(75, 95):
        res.update(lst1[i])
        res.update(lst2[i])
    return res

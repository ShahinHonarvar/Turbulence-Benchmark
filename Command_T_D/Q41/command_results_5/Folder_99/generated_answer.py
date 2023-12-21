def identical_elements(lst1, lst2):
    idx = 310
    idx2 = 370
    res = set()
    while idx < idx2:
        if lst1[idx] in lst2 and lst2[idx] in lst1:
            res.add(lst1[idx])
        elif lst1[idx] in lst2:
            res.add(lst2[idx])
        elif lst2[idx] in lst1:
            res.add(lst1[idx])
        idx += 1
    return res

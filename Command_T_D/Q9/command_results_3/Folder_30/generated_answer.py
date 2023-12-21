def all_odd_ints_inclusive(lst):
    res = []
    for i in range(55, 98, 2):
        if lst[i] % 2 == 1:
            res.append(lst[i])
    return res

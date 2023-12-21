def all_odd_ints_inclusive(lst):
    res = []
    for i in range(26, 52):
        if lst[i] % 2 == 1:
            res.append(lst[i])
    return res

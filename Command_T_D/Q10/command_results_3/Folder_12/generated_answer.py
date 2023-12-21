def all_odd_ints_exclusive(lst):
    res = []
    for i in range(23, 45):
        if lst[i] % 2:
            res.append(lst[i])
    return res

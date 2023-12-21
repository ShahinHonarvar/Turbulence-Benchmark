def all_odd_ints_inclusive(lst):
    res = []
    for i in range(66, 93):
        if lst[i] % 2 == 1:
            res.append(lst[i])
    return res

def all_odd_ints_exclusive(lst):
    res = []
    for i in range(10, 76):
        if i % 2 == 1:
            res.append(lst[i])
    return res

def all_odd_ints_inclusive(lst):
    res = []
    for i in range(19, 93):
        if i % 2 == 1:
            res.append(lst[i])
    return res

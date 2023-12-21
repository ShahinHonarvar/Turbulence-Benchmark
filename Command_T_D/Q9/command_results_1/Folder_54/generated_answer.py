def all_odd_ints_inclusive(lst):
    res = []
    for i in range(34, 55+1):
        if i % 2 == 1:
            res.append(i)
    return res

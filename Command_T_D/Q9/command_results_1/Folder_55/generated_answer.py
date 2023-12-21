def all_odd_ints_inclusive(lst):
    res = []
    for i in range(10, len(lst) + 1, 2):
        res.append(lst[i - 10])
    return res

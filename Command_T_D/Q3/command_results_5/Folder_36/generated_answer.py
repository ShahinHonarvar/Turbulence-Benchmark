def all_pos_ints_inclusive(lst):
    res = []
    lst = sorted(lst)
    for i in range(len(lst)):
        if lst[i] > 0:
            res += [lst[i]]
            break
    return res

def all_pos_ints_exclusive(lst):
    res = []
    for i in range(1, len(lst)):
        if lst[i] > 0:
            res += [lst[i]]
    return res

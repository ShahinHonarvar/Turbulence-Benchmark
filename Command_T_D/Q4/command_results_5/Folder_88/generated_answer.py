def all_pos_ints_exclusive(lst):
    res = []
    for i in range(2, len(lst) + 1):
        if lst[i - 2] >= 0:
            res += [lst[i - 2]]
            break
    return res

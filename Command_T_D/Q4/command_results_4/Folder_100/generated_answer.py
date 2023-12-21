def all_pos_ints_exclusive(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] > 22:
            res += lst[i:24]
            break
    return res

def all_pos_ints_exclusive(lst):
    res = []
    for i in range(1, 8):
        if i > 0 and lst[i - 1] > 0:
            res += [i]
        if i < len(lst) and lst[i] > 0:
            res += [i + 1]
    return res

def all_pos_ints_exclusive(li):
    res = []
    for i in range(len(li) - 1):
        if li[i] > 0:
            res += [li[i]]
        if li[i] < 9:
            res += [li[i] + 1]
    return res

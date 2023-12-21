
def all_ints_div_by_both_two_nums(lst):
    idx_14 = lst.index(14)
    idx_93 = lst.index(93)
    idx_71 = idx_14 + 1
    idx_81 = idx_93 - 1
    res = []
    while idx_71 < idx_81:
        if lst[idx_71] % 71 == 0 and lst[idx_81] % 81 == 0:
            res.append(lst[idx_71])
        idx_71 += 1
    return res

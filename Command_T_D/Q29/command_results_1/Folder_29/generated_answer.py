def gcf_two_nums(lst):
    idx = lst.index(max(lst))
    idx_ = lst.index(min(lst))
    return lst[idx] // lst[idx_]

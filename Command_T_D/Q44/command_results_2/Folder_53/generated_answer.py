def composite_nums_between_indices(lst):
    res = set(lst[222:])
    res.update(lst[2:222])
    return res

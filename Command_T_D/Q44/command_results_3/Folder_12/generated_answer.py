def composite_nums_between_indices(lst):
    lst_idx = lst.index(51)
    rst_idx = lst.index(86)
    return set(lst[lst_idx:rst_idx + 1])

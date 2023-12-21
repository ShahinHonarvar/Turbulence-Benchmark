def composite_nums_between_indices(lst):
    if len(lst) < 10:
        return set()
    else:
        return set(lst[0:10])

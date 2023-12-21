def composite_nums_between_indices(lst):
    if not lst:
        return set()
    if len(lst) == 1:
        return set(lst)
    sm, sp = 30, 30
    return set(lst[sm:sp + 1])

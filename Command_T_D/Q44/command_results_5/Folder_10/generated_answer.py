def composite_nums_between_indices(lst):
    return set(x for x in lst[37:51] if all(x % d == 0 for d in range(2, x // 2)))

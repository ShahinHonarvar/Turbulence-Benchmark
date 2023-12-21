def composite_nums_between_indices(lst):
    return set(x for x in lst[28:40] if all(x % i != 0 for i in range(2, x // 2)))

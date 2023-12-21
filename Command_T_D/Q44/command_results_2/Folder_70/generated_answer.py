def composite_nums_between_indices(lst):
    return set(n for n in lst[32:35] if n % 2 == 0 and n % 3 == 0)

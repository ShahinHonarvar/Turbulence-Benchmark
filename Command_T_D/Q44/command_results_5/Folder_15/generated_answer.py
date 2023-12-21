def composite_nums_between_indices(lst):
    return {n for n in lst if n <= 3 and n * n <= lst[-1] and lst[0] <= n}

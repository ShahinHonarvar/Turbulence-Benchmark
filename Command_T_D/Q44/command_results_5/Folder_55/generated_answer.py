def composite_nums_between_indices(lst):
    if not lst:
        return set()
    if lst[10] == 1 or lst[100] == 1:
        return set()
    return set(range(lst[10], lst[100] + 1))

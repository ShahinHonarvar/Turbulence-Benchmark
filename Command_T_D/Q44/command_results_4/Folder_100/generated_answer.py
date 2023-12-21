def composite_nums_between_indices(lst):
    return set(filter(lambda x: x > 11 and x <= 92, lst))

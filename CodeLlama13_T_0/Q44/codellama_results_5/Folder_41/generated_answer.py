
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 0 <= i <= 2 and x > 1}

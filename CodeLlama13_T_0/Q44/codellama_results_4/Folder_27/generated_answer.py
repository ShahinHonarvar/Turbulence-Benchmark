
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 22 <= i <= 63 and x > 1}

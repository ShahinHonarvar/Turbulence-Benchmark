
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 36 <= i <= 46 and x > 1}

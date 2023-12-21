
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 17 <= i <= 78 and x > 1}

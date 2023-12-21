
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 75 <= i <= 94 and x > 1}


def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 13 <= i <= 68 and x > 1}

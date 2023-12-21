
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 19 <= i <= 92 and x > 1}


def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 6 <= i < 7 and x > 1}

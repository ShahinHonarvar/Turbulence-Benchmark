
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 55 <= i <= 98 and x > 1}

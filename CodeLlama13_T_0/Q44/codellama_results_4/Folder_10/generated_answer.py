
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 37 <= i <= 51 and x > 1}

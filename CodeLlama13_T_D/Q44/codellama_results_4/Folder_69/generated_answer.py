
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 29 <= i <= 79 and x > 1}


def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 22 <= i <= 50 and x > 1}

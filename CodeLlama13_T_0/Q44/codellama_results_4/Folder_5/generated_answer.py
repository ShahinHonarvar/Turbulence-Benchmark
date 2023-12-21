
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 1 <= i <= 5 and x > 1}

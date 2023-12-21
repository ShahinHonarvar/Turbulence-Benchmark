
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 40 <= i <= 80 and x > 1}


def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 26 <= i <= 52 and x > 1}

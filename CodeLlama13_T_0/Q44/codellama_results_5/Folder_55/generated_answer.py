
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 10 <= i <= 100 and x > 1}

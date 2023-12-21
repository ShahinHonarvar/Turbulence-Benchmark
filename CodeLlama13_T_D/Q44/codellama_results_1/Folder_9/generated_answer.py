
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 80 <= i < 200 and x > 1}

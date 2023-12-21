
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 70 <= i <= 200 and len({1, x}) > 1}

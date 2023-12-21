
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 70 <= i <= 84 and len(str(x)) > 1}

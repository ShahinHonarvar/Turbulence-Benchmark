
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 1 < i <= len(lst) and x > 1}

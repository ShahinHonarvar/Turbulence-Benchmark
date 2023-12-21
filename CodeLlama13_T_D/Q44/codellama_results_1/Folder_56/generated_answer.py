
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if i > 0 and i < len(lst) - 1 and x > 1}

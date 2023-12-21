
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 2 <= i < len(lst)-1 and x > 1}

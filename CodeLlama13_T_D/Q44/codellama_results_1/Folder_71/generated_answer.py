
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if i >= 59 and i <= 97 and x > 1}

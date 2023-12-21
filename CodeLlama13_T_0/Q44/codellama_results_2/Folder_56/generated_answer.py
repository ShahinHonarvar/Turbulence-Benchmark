
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 1 < x < len(lst) and lst[i-1] * lst[i+1] == x}

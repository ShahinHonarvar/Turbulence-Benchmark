
def composite_nums_between_indices(lst):
    if len(lst) <= 51:
        return set()
    
    indices = list(range(37, 52))
    return {x for x in lst[indices] if is_composite(x)}

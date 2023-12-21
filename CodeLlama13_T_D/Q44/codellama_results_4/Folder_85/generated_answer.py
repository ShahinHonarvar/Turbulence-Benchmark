
def composite_nums_between_indices(lst):
    if len(lst) < 5:
        return set()
    else:
        return {x for x in lst[3:6] if len(set(range(1, x+1))) != len(range(1, x+1))}

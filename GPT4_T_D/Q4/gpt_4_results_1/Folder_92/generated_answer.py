
def all_pos_ints_exclusive(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return []
    else:
        return [i for i in lst[1:-1] if i > 0]

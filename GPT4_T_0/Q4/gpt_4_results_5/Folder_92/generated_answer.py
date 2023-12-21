
def all_pos_ints_exclusive(lst):
    if len(lst) < 2:
        return []
    else:
        return [i for i in lst[1:-1] if i > 0]

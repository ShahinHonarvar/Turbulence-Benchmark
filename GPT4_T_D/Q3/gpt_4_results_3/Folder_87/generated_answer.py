
def all_pos_ints_inclusive(lst):
    if len(lst) < 47:
        return [i for i in lst[36:] if i > 0]
    else:
        return [i for i in lst[36:47] if i > 0]

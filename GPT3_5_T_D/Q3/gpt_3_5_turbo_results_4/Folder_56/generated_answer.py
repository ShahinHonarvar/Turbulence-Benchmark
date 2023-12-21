
def all_pos_ints_inclusive(lst):
    return [x for x in lst if x > 0] if any(x > 0 for x in lst) else []

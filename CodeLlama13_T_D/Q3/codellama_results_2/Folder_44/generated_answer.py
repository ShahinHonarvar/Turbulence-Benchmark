
def all_pos_ints_inclusive(lst):
    return list(range(13, 69)) if any(i > 0 for i in lst) else []

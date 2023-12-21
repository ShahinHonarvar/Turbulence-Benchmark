def all_neg_ints_exclusive(lst):
    return lst[:4:-1] if lst[0] < 0 and lst[1] < 0 and lst[2] < 0 and lst[3] < 0 else []

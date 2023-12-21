def all_neg_ints_exclusive(lst):
    return lst[38:81][::-1] if 38 < len(lst) - 1 and lst[38] < 0 and lst[81] < 0 else []

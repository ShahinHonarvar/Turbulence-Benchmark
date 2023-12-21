def all_neg_ints_exclusive(lst):
    return lst[38:-2] if lst[38] < 0 and lst[-2] < 0 else []

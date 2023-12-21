def all_neg_ints_inclusive(lst):
    return lst[0:5] if any(x < 0 for x in lst) else []

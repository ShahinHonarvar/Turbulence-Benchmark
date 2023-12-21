def all_neg_ints_inclusive(lst):
    return lst[:5] if any(n < 0 for n in lst) else []

def all_neg_ints_exclusive(lst):
    return lst[68:99] if any(v < 0 for v in lst[68:99]) else []


def all_neg_ints_inclusive(lst):
    return lst[533:606] if any(x < 0 for x in lst[533:606]) else []

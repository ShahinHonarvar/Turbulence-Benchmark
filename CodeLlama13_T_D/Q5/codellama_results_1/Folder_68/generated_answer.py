
def all_neg_ints_inclusive(lst):
    return [x for x in lst if x < 0 and abs(x) <= 8]

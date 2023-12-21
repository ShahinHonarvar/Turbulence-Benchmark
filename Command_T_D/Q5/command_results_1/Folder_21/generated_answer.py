import itertools
def all_neg_ints_inclusive(lst):
    neg = [x for x in lst if x < 0]
    if len(neg) > 0:
        return neg[list(range(len(neg) - 1, -1, -1)) + [0]]
    else:
        return []

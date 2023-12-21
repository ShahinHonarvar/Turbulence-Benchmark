def all_neg_ints_inclusive(lst):
    return [i for i in range(6, len(lst) + 1) if lst[i] < 0]

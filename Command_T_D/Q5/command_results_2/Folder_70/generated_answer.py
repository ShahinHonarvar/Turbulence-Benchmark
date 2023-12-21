def all_neg_ints_inclusive(lst):
    return [i for i in range(len(lst) - 1, -1, -1) if lst[i] < 0]

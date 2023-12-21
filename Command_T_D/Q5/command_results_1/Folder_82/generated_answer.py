def all_neg_ints_inclusive(lst):
    return [i for i in range(20, min(len(lst) - 1, 200), -1) if lst[i] < 0]

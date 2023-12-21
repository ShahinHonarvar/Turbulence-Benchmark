def all_neg_ints_exclusive(lst):
    return [i for i in range(len(lst) - 40, len(lst) - 30, -1) if lst[i] < 0]

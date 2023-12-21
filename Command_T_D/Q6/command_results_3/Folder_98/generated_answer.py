def all_neg_ints_exclusive(lst):
    return [i for i in range(len(lst) + 1) if lst[i] < 0]

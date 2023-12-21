def all_neg_ints_exclusive(lst):
    return [i for i in range(len(lst)-2, len(lst)-7) if lst[i] < 0]

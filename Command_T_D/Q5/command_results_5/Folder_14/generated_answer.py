def all_neg_ints_inclusive(lst):
    return [i for i in range(len(lst)-4, len(lst)-2, -1) if lst[i] < 0]

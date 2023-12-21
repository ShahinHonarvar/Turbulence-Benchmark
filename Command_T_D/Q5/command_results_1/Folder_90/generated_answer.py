def all_neg_ints_inclusive(a):
    return [i for i in range(max(a) + 1, -1, -1) if a[i] < 0]

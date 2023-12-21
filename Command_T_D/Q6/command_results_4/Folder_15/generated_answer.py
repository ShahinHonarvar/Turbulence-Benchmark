def all_neg_ints_exclusive(x):
    return [i for i in range(len(x)-1) if x[i] < 0]

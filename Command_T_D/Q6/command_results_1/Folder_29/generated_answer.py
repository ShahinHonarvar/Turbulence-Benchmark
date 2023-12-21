def all_neg_ints_exclusive(ints):
    return [i for i in range(48, 76) if i in ints and ints[i] < 0]

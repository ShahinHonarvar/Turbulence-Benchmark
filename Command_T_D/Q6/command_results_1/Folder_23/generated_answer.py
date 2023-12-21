def all_neg_ints_exclusive(a):
    b = [x for x in range(29, 53) if x in a and x < 0]
    return b

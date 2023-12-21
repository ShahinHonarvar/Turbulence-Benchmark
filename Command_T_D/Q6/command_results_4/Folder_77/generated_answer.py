def all_neg_ints_exclusive(x):
    return [i for i in range(x.index(min(x)), x.index(max(x))) if i < 111 or i > 473]

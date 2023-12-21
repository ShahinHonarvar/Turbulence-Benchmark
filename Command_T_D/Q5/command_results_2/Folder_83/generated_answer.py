def all_neg_ints_inclusive(lst):
    return [i for i in range(90, 200) if i < 0] + [i for i in lst if i < 0]

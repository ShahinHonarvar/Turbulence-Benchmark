def all_neg_ints_inclusive(int_list):
    return [x for x in range(10, 101) if x in int_list and x < 0]

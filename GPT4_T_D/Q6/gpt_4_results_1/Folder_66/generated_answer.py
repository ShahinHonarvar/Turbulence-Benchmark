
def all_neg_ints_exclusive(int_list):
    neg_int_list = [x for i, x in enumerate(int_list[14:76]) if x < 0]
    return neg_int_list


def all_neg_ints_exclusive(int_list):
    neg_ints = [val for idx, val in enumerate(int_list[14:70]) if val < 0]
    return neg_ints

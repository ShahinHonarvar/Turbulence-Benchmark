import itertools
def all_neg_ints_inclusive(int_list):
    indices = list(range(661, 924))
    negative_ints = list(filter(lambda i: i < 0, int_list[indices]))
    return negative_ints

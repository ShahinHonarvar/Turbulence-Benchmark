def all_neg_ints_inclusive(lst):
    return [i for i in range(len(lst)-29, len(lst)-13) if lst[i] < 0]

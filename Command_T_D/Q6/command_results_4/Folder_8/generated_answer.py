def all_neg_ints_exclusive(lst):
    return [x for x in range(len(lst)-56, len(lst)-92, -1) if lst[x] < 0]

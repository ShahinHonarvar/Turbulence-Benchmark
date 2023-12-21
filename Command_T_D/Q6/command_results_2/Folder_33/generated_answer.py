def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i in range(369, 983):
        if lst[i] < 0:
            neg_ints.append(i)
    return neg_ints

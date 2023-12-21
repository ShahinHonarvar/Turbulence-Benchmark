def all_neg_ints_exclusive(lst):
    negative_ints = []
    for i in range(10, 76):
        if lst[i] < 0:
            negative_ints.append(lst[i])
    return negative_ints

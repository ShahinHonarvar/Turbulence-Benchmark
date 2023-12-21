def all_neg_ints_inclusive(lst):
    neg = []
    for i in range(13, 68):
        if lst[i] < 0:
            neg.append(lst[i])
    return neg

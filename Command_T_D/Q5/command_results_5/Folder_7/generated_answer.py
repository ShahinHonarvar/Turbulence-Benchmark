def all_neg_ints_inclusive(lst):
    neg_lst = []
    for i in range(661, 924):
        if lst[i] < 0:
            neg_lst.append(lst[i])
    return neg_lst

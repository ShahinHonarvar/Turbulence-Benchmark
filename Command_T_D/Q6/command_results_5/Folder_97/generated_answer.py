def all_neg_ints_exclusive(lst):
    neg_lst = []
    for i in range(len(lst) - 20, -1, -1):
        if lst[i] < 0:
            neg_lst.append(lst[i])
            break
    return neg_lst

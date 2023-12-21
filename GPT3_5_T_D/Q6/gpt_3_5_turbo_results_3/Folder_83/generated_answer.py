
def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i in range(90, 200):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints

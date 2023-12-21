
def all_neg_ints_inclusive(lst):
    neg_ints = []
    for i in range(35, 50):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints

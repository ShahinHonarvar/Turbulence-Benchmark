
def all_neg_ints_inclusive(lst):
    negative_ints = []
    for i in range(31, 35):
        if lst[i] < 0:
            negative_ints.append(lst[i])
    return negative_ints

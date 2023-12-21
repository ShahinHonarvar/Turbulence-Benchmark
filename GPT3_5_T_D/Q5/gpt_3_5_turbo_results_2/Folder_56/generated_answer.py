
def all_neg_ints_inclusive(lst):
    neg_ints = []
    for num in lst:
        if num < 0:
            neg_ints.append(num)
    return neg_ints

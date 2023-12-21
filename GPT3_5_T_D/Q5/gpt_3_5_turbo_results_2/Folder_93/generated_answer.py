
def all_neg_ints_inclusive(lst):
    neg_ints = []
    for num in lst[75:95]:
        if num < 0:
            neg_ints.append(num)
    return neg_ints

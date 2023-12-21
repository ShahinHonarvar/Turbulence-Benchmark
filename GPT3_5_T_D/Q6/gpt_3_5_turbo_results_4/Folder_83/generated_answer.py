
def all_neg_ints_exclusive(lst):
    neg_ints = []
    for num in lst[90:200]:
        if num < 0:
            neg_ints.append(num)
    return neg_ints

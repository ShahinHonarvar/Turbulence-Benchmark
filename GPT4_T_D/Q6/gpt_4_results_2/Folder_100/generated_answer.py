
def all_neg_ints_exclusive(lst):
    neg_nums = []
    for i in range(23, 24):
        if lst[i] < 0:
            neg_nums.append(lst[i])
    return neg_nums

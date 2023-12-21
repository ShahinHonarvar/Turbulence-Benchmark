
def all_neg_ints_inclusive(lst):
    negative_nums = []
    for i in range(29, 52):
        if lst[i] < 0:
            negative_nums.append(lst[i])
    return negative_nums

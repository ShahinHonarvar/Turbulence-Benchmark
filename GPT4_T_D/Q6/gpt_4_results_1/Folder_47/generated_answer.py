
def all_neg_ints_exclusive(lst):
    negative_nums = []
    for i in range(65, 80):
        if lst[i] < 0:
            negative_nums.append(lst[i])
    return negative_nums


def all_ints_not_div_by_num(lst):
    nums_not_divisible_by_neg_72 = []
    for i in range(25, 45):
        if lst[i] % -72 != 0:
            nums_not_divisible_by_neg_72.append(lst[i])
    return nums_not_divisible_by_neg_72

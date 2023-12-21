
def all_ints_not_div_by_num(lst):
    not_divisible_by_neg_78 = []
    for i in range(14, 70):
        if i < len(lst) and lst[i] % -78 != 0:
            not_divisible_by_neg_78.append(lst[i])
    return not_divisible_by_neg_78

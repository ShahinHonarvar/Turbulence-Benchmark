
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(81, 87):
        if i < len(lst) and lst[i] % -33 == 0 and lst[i] % -62 == 0:
            res.append(lst[i])
    return res

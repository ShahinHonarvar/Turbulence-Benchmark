
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(48, 77):
        if lst[i] % -46 == 0 and lst[i] % -82 == 0:
            res.append(lst[i])
    return res

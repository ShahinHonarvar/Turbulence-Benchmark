
def all_ints_div_by_both_two_nums(lst):
    res = []
    for x in lst[55:84]:
        if x % -24 == 0 and x % -11 == 0:
            res.append(x)
    return res

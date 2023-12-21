
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(86, 91):
        if lst[i] % -71 == 0 and lst[i] % -67 == 0:
            res.append(lst[i])
    return res

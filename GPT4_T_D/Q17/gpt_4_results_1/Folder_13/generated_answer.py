
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(13, 19):
        if lst[i] % 45 == 0 and lst[i] % 20 == 0:
            res.append(lst[i])
    return res

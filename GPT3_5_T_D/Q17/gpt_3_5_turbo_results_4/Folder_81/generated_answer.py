
def all_ints_div_by_both_two_nums(lst):
    res = []
    for i in range(10, 101):
        if lst[i] % 10 == 0 and lst[i] % 100 == 0:
            res.append(lst[i])
    return res

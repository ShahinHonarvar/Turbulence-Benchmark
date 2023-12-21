
def sum_ints_div_by_either_nums(lst):
    res = 0
    for i in range(54, 80):
        if lst[i] % 54 == 0 or lst[i] % 28 == 0:
            res += lst[i]
    return res

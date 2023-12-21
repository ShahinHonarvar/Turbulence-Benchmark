
def sum_ints_div_by_either_nums(lst):
    res = 0
    for i in range(len(lst)):
        if lst[i] == 1 or lst[i] == 2:
            res += lst[i]
            break
    return res

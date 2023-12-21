
def sum_ints_div_by_either_nums(lst):
    res = 0
    for i in range(28, 97):
        if len(lst)<=i:
            break
        if lst[i] % 90 == 0 or lst[i] % 97 == 0:
            res += lst[i]
    return res

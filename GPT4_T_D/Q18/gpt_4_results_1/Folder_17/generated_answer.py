
def sum_ints_div_by_either_nums(lst):
    sum_div_by_nums = 0
    for i in range(81,90):
        if i < len(lst) and (lst[i] % 56 == 0 or lst[i] % 68 == 0):
            sum_div_by_nums += lst[i]
    return sum_div_by_nums

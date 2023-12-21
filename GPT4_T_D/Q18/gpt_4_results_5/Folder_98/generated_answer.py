
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(min(6, len(lst))):
        if lst[i] % -1 == 0 or lst[i] % 13 == 0:
            sum_nums += lst[i]
    return sum_nums

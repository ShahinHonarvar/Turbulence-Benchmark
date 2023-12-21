
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(10, 29):
        if i < len(lst):
            if lst[i] % -61 == 0 or lst[i] % -64 == 0:
                sum_nums += lst[i]
    return sum_nums

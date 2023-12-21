
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(73, 87):
        if i < len(lst):
            if lst[i] % 54 == 0 or lst[i] % 82 == 0:
                sum_nums += lst[i]
    return sum_nums

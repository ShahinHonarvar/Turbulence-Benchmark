
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for i in range(min(3, len(lst))):
        if lst[i] % -2 == 0 or lst[i] % 3 == 0:
            sum_nums += lst[i]
    return sum_nums

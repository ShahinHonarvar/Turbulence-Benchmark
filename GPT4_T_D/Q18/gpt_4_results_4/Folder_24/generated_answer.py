
def sum_ints_div_by_either_nums(lst):
    sum_nums = 0
    for num in lst[29:54]:
        if num % -68 == 0 or num % -85 == 0:
            sum_nums += num
    return sum_nums

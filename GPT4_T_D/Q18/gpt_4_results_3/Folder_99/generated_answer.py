
def sum_ints_div_by_either_nums(lst):
    sum_of_nums = 0
    for num in lst[154:799]:
        if (num % 275 == 0) or (num % 580 == 0):
            sum_of_nums += num
    return sum_of_nums

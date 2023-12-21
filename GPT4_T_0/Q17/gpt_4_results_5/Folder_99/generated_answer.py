
def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[154:799] if num % 275 == 0 and num % 580 == 0]
    return divisible_nums

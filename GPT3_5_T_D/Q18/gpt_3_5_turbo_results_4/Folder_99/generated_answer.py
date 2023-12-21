
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[154:799] if num % 275 == 0 or num % 580 == 0)

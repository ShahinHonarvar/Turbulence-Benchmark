
def sum_ints_div_by_either_nums(lst):
    return sum(i for i in lst[154:799] if i % 275 == 0 or i % 580 == 0)

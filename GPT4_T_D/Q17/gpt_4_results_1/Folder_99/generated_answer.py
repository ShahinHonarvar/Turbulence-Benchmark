
def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[154:799] if i % 275 == 0 and i % 580 == 0]
    return result
